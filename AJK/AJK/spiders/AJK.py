# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from AJK.items import AjkItem

class AJK(scrapy.Spider):
    name = "AJK"
    start_urls = [
        'https://xa.fang.anjuke.com/',
    ]


    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        infos = soup.findAll(attrs={'class': 'item-mod'})
        for q in infos:
            if 'data-link' in str(q):
                item = AjkItem()
                item['title'] = q.h3.a.string
                print(q.h3.a.string)
                item['detailUrl'] = q.h3.a.get('href')
                print(q.h3.a.get('href'))
                item['locals'] = q.find(attrs={'class': 'address'}).a.string
                print(q.find(attrs={'class': 'address'}).a.string)
                if q.find(attrs={'class': 'price'}) != None:
                    item['price'] = q.find(attrs={'class': 'price'}).span.string
                    print(q.find(attrs={'class': 'price'}).span.string)
                else:
                    item['price'] = q.find(attrs={'class': 'favor-tag around-price'}).span.string+'around'
                    print(q.find(attrs={'class': 'favor-tag around-price'}).span.string+'around')
                item['telephone'] = q.find(attrs={'class': 'tel'}).string
                print(q.find(attrs={'class': 'tel'}).string)
                yield item





