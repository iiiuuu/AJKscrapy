# -*- coding: utf-8 -*-
import scrapy


class AJK(scrapy.Spider):
    name = "AJK"
    start_urls = [
        'http://xa.anjuke.com/',
    ]


    def parse(self, response):
        print(response.body)
