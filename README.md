# WebCrawler
This README.txt is written for users of Windows machines.

REQUIRED INSTALLATION:
  1. Python 2.7
  2. pip 
  3. lxml
  4. OpenSSL
  5. Scrapy 
  6. Selenium
  7. Firefox browser

For how to set up the above installation, refer to https://posnorm.com/2015/03/12/web-crawling-with-python-part-1-setup/


REQUIRED PYTHON FILES:
gdp_spider.py
indus_spider.py
taiex_spider.py
items.py : This is needed to crawl all data series. See Step 2 below.


TO IMPLEMENT THE WEB CRAWLER:
Step 0: 
Use the file 'project_name'_spider.py to crawl the data 'project_name'. 
For example, gdp_spider.py is used to crawl GDP, 
indus_spider.py is used to crawl Industrial Production Index,
and taiex_spider is used to crawl TAIEX price and volume.

Step 1: 
Open the command line window. 
Specify the working directory, then type -scrapy startproject 'project_name'-.
You should see a folder with the name 'project_name' in your working directory now. 
Type -cd 'project_name'- on the command window to change your working directory

Step 2: 
Under the folder, open the file named 'project_name'.py. 
Clear all the codes, and then copy and paste the codes from the ATTACHED file items.py. 
Change the class name to 'project_name'Item in the third line of the codes.
For example, to scrap GDP data, then type 'class cpiItem(scrapy.Item): 
Save.

Step 3:
Put 'project_name'_spider.py under the folder 'spiders' under the folder 'project_name'

Step 4:
Type -scrapy crawl 'project_name'_spider -o 'project_name'.csv -t csv- on the command line window.
Now you should see the file 'project_name'.csv in the folder. 



