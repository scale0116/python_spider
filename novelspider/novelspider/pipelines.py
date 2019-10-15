# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class NovelspiderPipeline(object):

    def process_item(self, item, spider):
        # try:
        #     os.mkdir(r'D:\Novels\test')
        # except:
        #     pass
        res = dict(item)
        title = res['title'][0]
        content_list = res['content']
        with open(r'D:\Novels\test.txt', 'a+', encoding='utf-8') as f:
            f.writelines(title + '\n')
            for content in content_list:
                content = content.replace('\xa0'*4,'')
                f.writelines(content + '\n')
        # txt_path = 'D:/Novels/test/' + title + '.txt'
        # with open(txt_path, 'a+', encoding='utf-8') as f:
        #     f.writelines(title + '\n')
        #     for content in content_list:
        #         content = content.replace('\xa0'*4,'')
        #         f.writelines(content + '\n')

        return item
