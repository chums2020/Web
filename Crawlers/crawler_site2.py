import re 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #necessary, otherwise the except NoSuchElementException statement cannot catch error
from selenium.common.exceptions import TimeoutException
import time
import csv
import sys
import urllib2
from urllib2 import URLError

reload(sys)
sys.setdefaultencoding('utf-8')

pages = [] #a list that stores all url links
init_pages = []
invalid_pages = [] #a list that stores url links that output an error
driver = webdriver.Firefox() #initialize a Firefox browser
driver.set_page_load_timeout(10)
for i in range(71, 101): #sets the number of web pages to be scraped
    while True:
        try:
            driver.get("http:/XXXXX/?inweek=1&page="+str(i))
            time.sleep(2)
            items = driver.find_elements_by_xpath("//*[@href]")
            for item in items:
                page = item.get_attribute('href') #store all html links
                href = re.compile("^(http://XXXXX/usedauto-infos-)[0-9]+(.html)$") #regular expression criterion
                if re.match(href, page): #if the url link meets the regular expression criteria
                    if page not in pages: #and if the page is not already appended
                        pages.append(page) #append the url link in the list
        except TimeoutException:
            print "Timeout, retrying..."
            continue
        else:
            init_pages.append("http://XXXXX/?inweek=1&page="+str(i))
            break


print "URLs that have succesfully added"
print pages

print "Initial URLs that have succesfully added"
print init_pages


csvFile= open('crawl_data5.csv','wb') #open a csv file that will stored data
csvFile.write(u'\ufeff'.encode('utf8')) #ensure encoding for data written to csv
writer = csv.writer(csvFile)
#first row (header)
writer.writerow(('ID','price','brand','model','year','color','size (cc)','city','transmission','fuel','engine','license_date','door','seat','mileage'))

def scrapLink(newUrl):
    while True:
        try:
            driver.get(newUrl) # go to the new site

        except TimeoutException:
            print "Timeout, retrying..."
            continue
        else:
            time.sleep(2)
            break

    try:
        items = driver.find_element_by_class_name("mb-info")
        infos = items.find_elements_by_xpath("//ul/li/span")
        price = items.find_element_by_xpath("//ul/li/div/b").text
        url_id = int(re.findall(r'\d+', newUrl)[1]) #extract id numbers from url
        print "{0}\t{1}".format(url_id, price)
        for i in range(0, 13):
            print infos[i].text.encode('utf-8') # print all auto information
        #write the data to the csv file
        writer.writerow((url_id, price, infos[0].text, infos[1].text, infos[2].text, infos[3].text, infos[4].text, infos[5].text, infos[6].text, infos[7].text, infos[8].text, infos[9].text, infos[10].text, infos[11].text, infos[12].text))

    except AttributeError:
        print("Attribute Error. This page is missing something! "+ newUrl)
        invalid_pages.append(newUrl)
    except IndexError:
        print("Index Error. This page is missing something! " + newUrl)
        invalid_pages.append(newUrl)
    except NoSuchElementException: #if this is the case, price data are probably missing
        print("NoSuchElementException. This page is missing something! "+ newUrl)
        invalid_pages.append(newUrl)

for page in pages:
    scrapLink(page) #throw each Url in the list pages in self-defined function scrapLink

csvFile.close() #finally, close the csv file
