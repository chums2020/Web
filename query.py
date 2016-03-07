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




