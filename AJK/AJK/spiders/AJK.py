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
        #数据信息列
        infos = soup.findAll(attrs={'class': 'item-mod'})
        # 分页部分
        pagesUrl = soup.find(attrs={'class': 'list-page'})
        print("开始计算页码个数")
        # 楼盘总数
        number = int(pagesUrl.find(attrs={'class': 'total'}).em.string)
        # 页码总数其中每页固定50个数据
        pages = number // 50
        if (number % 50 > 0):
            pages = pages + 1
        print("一共" + str(pages))
        purl = pagesUrl.find(attrs={'class': 'pagination'}).a['href']
        purl = purl[0:-3]
        for i in range(1, pages + 1):
            temp = purl + "p" + str(i) + "/"
            print("生成需要爬去的页面链接" + temp)
            print("发送请求" + temp)
            yield scrapy.Request(temp, callback=self.parse_item)
            print("处理数据完毕")

    def parse_item(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        # 数据信息列
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
                    item['price'] = q.find(attrs={'class': 'favor-tag around-price'}).span.string + 'around'
                    print(q.find(attrs={'class': 'favor-tag around-price'}).span.string + 'around')
                item['telephone'] = q.find(attrs={'class': 'tel'}).contents[1]
                print(q.find(attrs={'class': 'tel'}).string)
                yield item




