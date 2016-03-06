import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from indus.items import indusItem
import unicodecsv as csv

class indus_spider(scrapy.Spider):
    name = 'indus_spider'
    allowed_domains = ['statdb.dgbas.gov.tw/']
    start_urls = ['http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=ES0104A1M&ti=%A4u%B7~%A5%CD%B2%A3%AB%FC%BC%C6-%A4%EB&path=../PXfile/EconomicStatistics/&lang=1&strList=L']
 
    def __init__(self):
        self.driver = webdriver.Firefox()
 
    def parse(self, response):
        items = []
        item = indusItem()
 
        driver = self.driver
        driver.get(response.url)
        driver.find_element_by_partial_link_text('Select all').click()
        driver.find_element_by_css_selector('select[name="values2"]>option[value="1"]').click()
        driver.find_element_by_css_selector('select[name="values3"]>option[value="1"]').click()

        driver.find_element_by_xpath('//input[@type="SUBMIT"]').click()

        hxs = HtmlXPathSelector(text=self.driver.page_source)
        data = hxs.xpath("//table[@class='pxtable']//tbody//tr")
     
        for datum in data:

            item ["date"] = datum.xpath('td[1]/text()').extract()
            item ["data"] = datum.xpath('td[2]/text()').extract()

            yield item


     
       
     