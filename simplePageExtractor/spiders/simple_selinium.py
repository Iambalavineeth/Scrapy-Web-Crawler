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

#Scrapy Class
class CrawlerSpider(scrapy.Spider):
    #Spider Name
    name = "selspider"
    #Giving List of Starting URLs
    start_urls = ['http://forum.nafc.org/login/']

    #Constructor Class - Initializing the Firefox Web Driver
    def __init__(self, filename=None):
        self.driver = webdriver.Firefox()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    #Close the Spider
    def spider_closed(self, spider):
        self.driver.close()

    #Main Parse function for getting the urls
    def parse(self, response):
        # Load the current page into Selenium
        self.driver.get(response.url)
        username = self.driver.find_element_by_id('registerUserName')
        password = self.driver.find_element_by_id('registerPass')

        #Giving the Username and Password
        username.send_keys("username")
        password.send_keys("passwd")

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
