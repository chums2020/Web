#put all raw csv files under the directory crawler and the subdirectory raw

import re 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #necessary, otherwise the except NoSuchElementException statement cannot catch error
from selenium.common.exceptions import TimeoutException
import time
import csv
import sys
import urllib2
from urllib2 import URLError
import os
from random import randint

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox() #initialize a Firefox browser
driver.set_page_load_timeout(10)

def scrapLink(url):
    i = 0
    while True:
        i = i + 1
        if i > 10:
            print "retried 10 times, skip and break"
            break
        try:
            driver.get(url) # go to the new site
            time.sleep(randint(5,15))
            brand = driver.find_element_by_xpath("//span[contains(@data-reactid, '$/=10.0.0.0.1.1')]").text
            series = driver.find_element_by_xpath("//span[contains(@data-reactid, '$/=10.0.0.0.1.3')]").text
            category = driver.find_element_by_xpath("//span[contains(@data-reactid, '$/=10.0.0.0.1.5')]").text
            year = driver.find_element_by_xpath("//span[contains(@data-reactid, '$/=10.0.0.0.1.7')]").text
            #print brand, series, category, year
        except TimeoutException:
            print "Timeout, retrying..."
            continue
        except NoSuchElementException:
            print "No such element exception, retrying..."
            continue
        else:
            #time.sleep(randint(2,5)) #sleep for a random amount of time
            break

    try:
        p1 = driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$0.1.0')]").text
        p2 =  driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$0.1.2')]").text
    except:
        p1 = None
        p2 = None
    try:
        p3 = driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$1.1.0')]").text
        p4 = driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$1.1.2')]").text
    except:
        p3 = None
        p4 = None
    try:
        p5 = driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$2.1.0')]").text
        p6 = driver.find_element_by_xpath("//span[@class='price' and contains(@data-reactid, '$2.1.2')]").text
    except:
        p5 = None
        p6 = None

    writer.writerow((brand, category, series, year, p1, p2, p3, p4, p5, p6))


content_list = []
for content in os.listdir("./raw"): # "." means current directory
    content_list.append(content)

print content_list

for input_filename in content_list:
    #with open(input_filename, 'rb', encoding='utf-8') as f: #read file in current directory
    with open(input_filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    ouput_filename = input_filename
    csvFile= open(ouput_filename,'wb') #open a csv file that will stored data
    csvFile.write(u'\ufeff'.encode('utf8')) #ensure encoding for data written to csv
    writer = csv.writer(csvFile)
    #first row (header)
    writer.writerow(('ID',"category","series","year","price1","price2","price3","price4","price5","price6"))

    for i in range(1, len(your_list)):
        brandID = your_list[i][0]
        series = your_list[i][1]
        category = your_list[i][2].decode('big5-tw')
        for year in range(1997, 2017):
            url = "http://XXXXX_BrandID="+ brandID+"&Category="+category+ "&Series="+ series+ "&Year="+ str(year)
            scrapLink(url)

    csvFile.close()
