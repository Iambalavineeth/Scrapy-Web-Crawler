# Scrapy-Web-Crawler

## Details:
This is a Web Crawler project to build a one-stop shop application for caregivers and patients to easily access relevant information based on various categories. This project is done with the Clemson University - Nursing Department to better analyze the problems faced by patients suffering from Incontinence and Alzheimer's.

## Websites:
* Alzheimer's ALZ Connected Website: https://www.alzconnected.org/
* Incontinence NAFC Website: http://forum.nafc.org/

## Web Scraping Details:
Till now I have collected around 2700 posts from NAFC website and more than 200k posts from ALZ Connected Website. These posts will be categorized based on main categories provided by the Clemson University - Nursing Department. We will also be making use of Machine Learning algorithms to identify main taking points from the posts collected.

## Running the Spiders:
To run the spiders for extracting posts from the above mentioned websites. First go inside the project, in this case it is *simplePageExtractor*

* Normal Run:
```
scrapy crawl <spider-name>
```
* Collect the posts in a CSV File:
```
scrapy crawl <spider-name> -t csv -o <csv-name>.csv
```
