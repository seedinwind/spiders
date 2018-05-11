# -*- coding: utf-8 -*-

import scrapy
from helloscrapy.items import PoemAuther


class PoemSpider(scrapy.Spider):
    name = 'poem'
    allowed_domains = ['www.53reniao.com']
    start_urls = [
        'https://so.gushiwen.org/authors/',
        # 'https://so.gushiwen.org/authors/authorvsw_1abe13750637A1.aspx',
    ]

    def start_request(self):
        yield scrapy.Request(start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        base_url = 'https://so.gushiwen.org'
        base_auther_url='https://so.gushiwen.org/authors/'
        if (response.url==base_auther_url) |response.url.startswith('https://so.gushiwen.org/authors/default'):
            #作者列表
            list=response.xpath("//div[@class='main3']/div[@class='left']/div[@class='sonspic']/div[@class='cont']")
            name=list.xpath(".//p[1]/a[1]/b/text()").extract()
            desc=list.xpath(".//p[2]/text()").extract()
            poemlist=list.xpath(".//p[2]/a/@href").extract()
            next=response.xpath("//div[@class='main3']/div[@class='left']/form/div/a[1]/@href").extract()
            yield scrapy.Request(base_url+next[0], callback=self.parse, dont_filter=True)
            #保存作者信息
            for n in range(0 ,len(name)-1):
                item=PoemAuther()
                item['name']=name[n]
                item['desc']=desc[n]
                yield item
            for poem in poemlist:
                yield scrapy.Request(base_url + poem, callback=self.parse, dont_filter=True)

        elif response.url.startswith('https://so.gushiwen.org/authors/authorvsw'):

             print("----------------"+response.url+"----------------------")
             #作品列表
             list = response.xpath("//div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']")
             title = list.xpath(".//p[1]/a[1]/b/text()").extract()
             time = list.xpath(".//p[2]/a[1]/text()").extract()
             poemist = list.xpath(".//p[2]/a[2]/text()").extract()
             content = list.xpath(".//div[@class='contson']")
             #拼接正文内容
             contentlist=[]
             for i in range(0,len(content)-1):
                lines=content[i].xpath(".//p/text()|.//text()").extract()
                concat=""
                for l in lines:
                    concat+=l
                contentlist.append(concat)
                print(title[i])
                print(time[i]+"  "+poemist[i])
                print(concat)

