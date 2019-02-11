def get_web(url):
    import requests
    raw_html = requests.get(url).content.decode('utf-8')
    return raw_html

def get_contents_title(html,cls_name):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    title_objs = soup.select(cls_name)
    contents_list=[title_obj.h5.get_text().replace('/','').replace('.','') for title_obj in title_objs]
    return contents_list