# WebCrawler
This README file is written for users of Windows machines.

**REQUIRED INSTALLATION:**  
  1. Python 2.7
  2. pip 
  3. lxml
  4. OpenSSL
  5. Scrapy 
  6. Selenium
  7. Firefox browser

For how to set up the above installation, refer to https://posnorm.com/2015/03/12/web-crawling-with-python-part-1-setup/


**REQUIRED PYTHON FILES:**
  1. gdp_spider.py
  2. indus_spider.py
  3. taiex_spider.py
  4. items.py : This is needed to crawl all data series. See Step 2 below.


**TO IMPLEMENT THE WEB CRAWLER:**  
_Step 0:_  
  Use the file 'project_name'_spider.py to crawl the data 'project_name'.   
  For example, gdp_spider.py is used to crawl GDP, indus_spider.py is used to crawl Industrial Production Index, and taiex_spider is used to crawl TAIEX price and volume.

_Step 1:_  
  Open the command line window.  
  Specify the working directory, then type -scrapy startproject 'project_name'-.  
  You should see a folder with the name 'project_name' in your working directory now.  
  Type -cd 'project_name'- on the command window to change your working directory.  

_Step 2:_  
  Under the folder, open the file named 'project_name'.py.  
  Clear all the codes, and then copy and paste the codes from the ATTACHED file items.py.  
  Change the class name to 'project_name'Item in the third line of the codes.  
  For example, to scrap GDP data, then type 'class gdpItem(scrapy.Item):'  
  Save.

_Step 3:_  
  Put 'project_name'_spider.py under the folder 'spiders' under the folder 'project_name'  

_Step 4:_  
  Type -scrapy crawl 'project_name'_spider -o 'project_name'.csv -t csv- on the command line window.  
  Now you should see the file 'project_name'.csv in the folder.  



