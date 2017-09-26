import scrapy
import selenium
import time

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.http import TextResponse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CrawlerSpider(scrapy.Spider):
    name = "selspider"
    start_urls = ['http://forum.nafc.org/login/']

    def __init__(self, filename=None):
        self.driver = webdriver.Firefox()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        self.driver.close()

    def parse(self, response):
        # Load the current page into Selenium
        self.driver.get(response.url)
        username = self.driver.find_element_by_id('registerUserName')
        password = self.driver.find_element_by_id('registerPass')

        username.send_keys('helloworld123')
        password.send_keys('helloworld123')

        self.driver.find_element_by_name("registerButton").click()
        #Click the Show More Button for 5 times
        for i in range(5):
            self.driver.find_element_by_xpath('//div[@id="moreButton"]/div[@class="moreThreads"]/a').click()
            time.sleep(2)

        # Sync scrapy and selenium so they agree on the page we're looking at then let scrapy take over
        response = TextResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')

        # scrape as normal
        url_list = response.xpath('//a[contains(@href, "topic")]/@href').extract()
        self.log(url_list)
        
