'''
This is a Web Crawler for Alzheimer's ALZ Connected Website - A Care giving website where users post about ALZ
ALZ Caregiver's Website ---- https://www.alzconnected.org/
'''

import scrapy
import re

#Scrapy Class
class ALZSpider2(scrapy.Spider):
    #Spider Name
    name = "ALZSpider"
    #Giving List of Starting URLs
    start_urls = [
        "https://www.alzconnected.org/discussion.aspx?g=topics&f=151"
        ]

    #Parsing the first page of Caregiver's form
    def parse(self, response):
        yield response.follow(response.url, callback=self.parse_page)

    #Recursively calling the other pages of the Caregiver's form
    def parse_page(self, response):
        #Getting URLs for the page
        thread_urls = response.xpath('//tr[contains(@class, "post")]/td[2]/a/@href').extract()
        #Going inside each URL - Threads in a single page
        for thread_url in thread_urls:
            self.foundPages = False
            yield response.follow(thread_url, callback=self.parse_threads)
        #Checking for a next pages and parsing them recursively
        page_after = response.xpath('//td[contains(@class, "header1")]/span/a[@class="ekforumpagelink" and text()="Next"]/@href').extract()
        if(page_after):
            yield response.follow(page_after[0], callback=self.parse_page)

    #Parsing a Thread
    def parse_threads(self, response):
        nav_thread_pages = response.xpath('//div[contains(@class, "pagenav")]/table//td[contains(@class, "alt2")]/a/@title').extract()
        if(nav_thread_pages):
            last_thread_page_num =  int(nav_thread_pages[-1:][0].split(" ")[-1:][0])
        else:
            last_thread_page_num = 1
        #Crawling all the thread pages
        for thread_page_num in range(1, last_thread_page_num+1):
            next_thread_page_url = response.url + "&page=" + str(thread_page_num)
            self.log(next_thread_page_url)
            yield response.follow(next_thread_page_url, callback=self.parse_thread_page)

    #Parsing posts on a Single Thread Page
    def parse_thread_page(self, response):
        thread_heading = response.xpath('//td[contains(@class, "header1")]//td[1]/text()').extract()[0]
        post_content_unordered = response.xpath('//tr[contains(@class, "post")]//text()').extract()
        post_content_unordered = [elem.encode('utf-8') for elem in post_content_unordered]
        filtered_posts = []
        pattern = re.compile(r"[a-zA-Z]+")
        for elem in post_content_unordered:
            if pattern.search(elem):
                filtered_posts.append(elem)
        count = 0
        particular_post = []
        for i in filtered_posts:
            if i != "Back to top":
                particular_post.append(i)
            else:
                if count == 0:
                    question = "YES"
                    count += 1
                else:
                    question = "NO"
                yield{
                    'THREAD_HEADING' : thread_heading,
                    'USER' : particular_post[0].strip(),
                    'POST_DATE' : particular_post[2].strip(),
                    'USER_JOIN_DATE' : particular_post[3].strip(),
                    'USER_PROFILE_POSTS' : particular_post[4].strip(),
                    'POST_CONTENT' : ''.join(particular_post[5:]).strip(),
                    'QUESTION' : question,
                }
                particular_post = []
                print "***************"

if __name__ == "__main__":
    spider = ElementSpider()
