# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class AjkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 楼盘名称
    title = Field()
    # 楼盘位置
    locals = Field()
    # 楼盘价格（只是均价）
    price = Field()
    # 楼盘联系方式
    # telephone = Field()
    # 楼盘链接
    detailUrl = Field()


