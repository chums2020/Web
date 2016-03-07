#Reference: Intro to Computer Science Lesson 1- 3, Udacity
seed = ['','',''] #seed pages

#transform url to HTML source code 
def get_page(page): 
    
  

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

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:#if tocrawl ==[], return FALSE
        page = tocrawl.pop() #Depth-Furst Search: the last link is searched first
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(get_page(page))
    return crawled
        


print get_all_links(get_page(page))
