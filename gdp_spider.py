import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from gdp.items import gdpItem
import unicodecsv as csv

class gdp_spider(scrapy.Spider):
    name = 'gdp_spider'
    allowed_domains = ['statdb.dgbas.gov.tw/']
    start_urls = ['http://statdb.dgbas.gov.tw/pxweb/Dialog/varval.asp?ma=NA8101A1Q&ti=Principal%20Figures%282008SNA%29-Quarterly&path=../PXfileE/NationalIncome/&lang=1&strList=L']

    def __init__(self):
        self.driver = webdriver.Firefox()
 
    def parse(self, response):
        items = []
        item = gdpItem()
        driver = self.driver
        driver.get(response.url)

        driver.find_element_by_partial_link_text('Select all').click()
        driver.find_element_by_xpath('//option[contains(text(),"GDP (Million N.T.$,at Current Prices)")]').click()
        driver.find_element_by_xpath('//option[contains(text(),"Data")]').click()
        driver.find_element_by_xpath('//input[@type="SUBMIT"]').click()

        hxs = HtmlXPathSelector(text=self.driver.page_source)
        data = hxs.xpath("//table[@class='pxtable']//tbody//tr")
     
        for datum in data:       
            item ["date"] = datum.xpath('td[1]/text()').extract()
            item ["data"] = datum.xpath('td[2]/text()').extract()

            yield item
     


     
       
     
        