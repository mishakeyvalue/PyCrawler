import requests
from bs4 import BeautifulSoup as bf

log_path = r"c:\users\mitutee\documents\pricing_comfy.txt"
lf = open(log_path, 'a')

def analyse_goods(tag):
    
    # Dealing with stats
    try:   
        RAM = tag.findAll('dl')[1].find('dd').text.strip()
        HDD = tag.findAll('dl')[2].find('dd').text.strip()
        PRICE = tag.find('span', {'class': 'price-value'}).text.strip()
        MODEL = tag.find('a').get('title')
        #lf.write('Price = {0}, Model: {1}, RAM = {2}, HDD = {3}\n'.format(PRICE, MODEL, RAM, HDD))
        print('Price = {0}, Model: {1}, RAM = {2}, HDD = {3}\n'.format(PRICE, MODEL, RAM, HDD))
    except IndexError:
        print("Wrong index..")
    except:
        raise
    
def core_spider(max_pages):
    page = 1
    while page < max_pages:   
        _url = "http://comfy.ua/notebook/?p="+str(page)
        
        data = requests.get(_url)
        plain_text = data.text.encode('utf-8')
        soup = bf(plain_text, "html.parser")
        
        for el in soup.findAll('table',{'class': 'content'}):
            analyse_goods(el)                  
             
        page+=1
    lf.close()


core_spider(14 )


