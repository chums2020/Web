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
    
def print_all_links(page):
    while page!="":
        url, end_point = get_next_target(page)
        if url:
            print url
            page = page[end_point:]
        else:
            break

page = ""  #Insert HTML source code 
print_all_links(page)
