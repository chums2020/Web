import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from taiex.items import taiexItem
import unicodecsv as csv

class taiex_spider(scrapy.Spider):
    name = 'taiex_spider'
    allowed_domains = ['finance.yahoo.com/']
    start_urls = ['http://finance.yahoo.com/q/hp?s=^TWII&a=00&b=15&c=2004&d=11&e=4&f=2015&g=m']

    def __init__(self):
        self.driver = webdriver.Firefox()
 
    def parse(self, response):
        items = []
        item = taiexItem()
        driver = self.driver
        driver.get(response.url)
        driver.find_element_by_css_selector('select[id="selstart"]>option[value="00"]').click()     
        driver.find_element_by_css_selector('select[id="selend"]>option[value="11"]').click()
        start_year = driver.find_element_by_id("startyear")
        start_year.clear()
        start_year.send_keys("2004")
        end_year = driver.find_element_by_id("endyear")
        end_year.clear()
        end_year.send_keys("2015")

        start_day= driver.find_element_by_id("startday")
        start_day.clear()
        start_day.send_keys("15")
        end_day = driver.find_element_by_id("endday")
        end_day.clear()
        end_day.send_keys("15")
        
        driver.find_element_by_id("monthly").click()
        time.sleep(2)
        driver.find_element_by_xpath('//input[@value="Get Prices"]').click()
        time.sleep(3)
        driver.find_element_by_partial_link_text('Download to Spreadsheet').click()

        
