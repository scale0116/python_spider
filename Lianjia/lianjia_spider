# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:32:26 2018

@author: ShiJichen
"""

import requests, random, time
import pandas as pd
from lxml import etree

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

pages=['https://su.lianjia.com/ershoufang/gongyeyuan/pg{}/'.format(x) for x in range(1,100)]
############################################################

#aim_url = 'https://su.lianjia.com/ershoufang/gongyeyuan/pg1/'
def lianjia_parse(aim_url):
    html = requests.get(url=aim_url, headers=hds[random.randint(0,len(hds)-1)]).content
    element = etree.HTML(html)
    house_info = element.xpath("//div[@class='info clear']//div[@class='houseInfo']/a/text()")
    house_description = element.xpath("//div[@class='info clear']//div[@class='houseInfo']/text()")
    house_price = element.xpath("//div[@class='totalPrice']/span/text()")
    house_position = element.xpath("//div[@class='positionInfo']/text()")
    house_region = element.xpath("//div[@class='positionInfo']/a/text()")
    house_follow = element.xpath("//div[@class='followInfo']/text()")
    #print(house_info)
    info_list =[]
    for i in range(len(house_info)):
        item = {}
        item['小区'] = house_info[i]
        item['价格'] = house_price[i]
        description = house_description[i].split('|')
        item['户型'] = description[1]
        item['面积'] = description[2].replace('平米','')
        item['朝向'] = description[3]
        item['装修'] = description[4]
        try:
            item['电梯'] = description[5]
        except:
            item['电梯'] = description[4]
        try:
            item['楼层'] = house_position[i].split(')')[0] + ')'
            item['建造时间'] = house_position[i].split(')')[1]
        except:
            item['楼层'] = house_position[i]
            item['建造时间'] = house_position[i]
        item['区域'] = house_region[i]
        item['关注人数'] = house_follow[i].split('/')[0]
        item['带看人数'] = house_follow[i].split('/')[1]
        item['发布时间'] = house_follow[i].split('/')[2]
        df = pd.DataFrame.from_dict(item, orient='index').T
        info_list.append(df)
    df_list = pd.concat(info_list,ignore_index=True)
    return df_list
    #df_list.to_excel(r'D:\Python\codes\Lianjia_spider\test.xlsx')

if __name__ == '__main__':    
    count = 0
    final_data = pd.DataFrame(columns=['小区','价格','户型', '面积', '朝向', '装修', '电梯', '楼层', '建造时间', '区域', '关注人数', '带看人数', '发布时间'])
    for page in pages:
        df_list = lianjia_parse(page)
        count = count + 1
        print ('Page ' + str(count) + ' is sucessful')
        final_data = pd.concat([final_data, df_list], ignore_index=True)
        time.sleep(random.randint(0,5))
    final_data.to_excel(r'D:\Python\codes\Lianjia_spider\test.xlsx')
