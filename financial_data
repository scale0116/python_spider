# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:35:33 2018

@author: Shi Jichen
"""

from bs4 import BeautifulSoup
import requests, time, random, urllib, os


def download_data(stock, url):
    DATA_PATH = os.path.join(os.getcwd(), '%s/' %stock)
    
    hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
        {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
        {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
        {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
        {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
        {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
        {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
        {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
        {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
        {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]
    
    time.sleep(random.randint(0,5))
    response = requests.get(url=url, headers=hds[random.randint(0,len(hds)-1)])
    content = response.content.decode()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    financial_data_list = soup.find_all(name='a', class_='download_link', id = 'downloadData')
    raw_title_list = soup.find_all(name = 'span', class_ = 'name')
    title_list = []
    
    for title_item in raw_title_list:
        title_list.append(title_item.text.replace('<span class="name">','').replace('</span>',''))
    download_link_list = []
    for item in financial_data_list:
        href = item.attrs['href']
        download_link = 'http://quotes.money.163.com' + href
        download_link_list.append(download_link)
    print(title_list)
    
    try:
        os.mkdir(DATA_PATH)
    except:
        pass
    for i in range(len(download_link_list)):
        file_name = DATA_PATH + title_list[i] + '.csv'
        time.sleep(random.randint(0,5))
        urllib.request.urlretrieve(download_link_list[i], file_name)
        print('%s已下载完成' %title_list[i])

if __name__ == '__main__':
    stock_list = ['600028', '601939', '601398']
    for stock in stock_list:
        url = 'http://quotes.money.163.com/f10/zycwzb_' + stock + '.html#01c01'
        download_data(stock, url)
