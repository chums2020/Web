#Reference: Intro to Computer Science, Udacity
seed = ['','',''] #seed pages

#transform url to HTML source code 
def get_page(page): 
    try: #try block
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
  

def get_next_target(page):
    start_link = page.find('<a href =')
    if start_link ==-1
        return "None", 0
        break
    start_quote = page.find('"', start_link)
    end_quote= page.find('"', start_quote+1)
    url =page(start_quote+1:end_quote)
    print(url)
    return end_quote, url

    page = page[end_quote:]
    
def get_all_links(page):
    links = []   #empty list
    while page!="":
    url, end_point = get_next_target(page)
    if url:
        links.append(url)
        page = page[end_point:]
    else:
        break
    return links

def union(a,b):#assume a is already a set, i.e.,no repetitive element
    for e in b:
        if e not in a:
            a.append(e)

#an index is a list [[keyword1,[url1,url2,...]],[keyword2,[url1,url2,...]],...]
#add_to_index add the keyword and associated url to index if the keyword is not already in the index

def add_to_index(index,keyword,url):
    i=0
    for e in index:
        if keyword in e:
            index[i][1].append(url)
            return
        i = i+1
    index.append([keyword,[url]])

#lookup returns the list of urls associated with the keyword

def lookup(index,keyword):
    for e in index:
        if e[0]==keyword:
            return e[1]
    return []

#add_page_to_index add the web content to the index

def add_page_to_index(index,url,content):
    words = content.split() #split the web content into a list of words
    for word in words:
        add_to_index(index,word,url)
    return index


index = []
add_page_to_index(index,"https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-2#!","""
Never learned Linux? Want a refresh? 
Take this course free or get a verified certificate for $99 
""")



def crawl_web(seed, max_pages, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    index=[]
    while depth<= max_depth and len(crawled)<max_pages:#if tocrawl ==[], return FALSE
        page = tocrawl.pop() #Depth-Furst Search: the last link is searched first
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(next_depth, get_all_links(content))
            crawled.append(get_page(page))
        if not tocrawl: #if tocrawl if empty
            tocrawl, next_depth = next_depth, []
            depth = depth +1
            if next_depth ==[]:
                break
    return index
