# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from AJK.items import AjkItem

class AjkPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
    # 将爬到的数据存入数据库
    def process_item(self, item, spider):
        """ 判断类型 存入MongoDB """
        print("开始存储数据"+item['title'])
        if isinstance(item, AjkItem):
            print("数据类型一致")
            try:
                self.coll.insert(dict(item))
            except Exception:
                pass
        return item



