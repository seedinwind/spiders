# -*- coding: utf-8 -*-

import scrapy


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
        if (response.url==base_auther_url) |response.url.startswith('https://so.gushiwen.org/authors/Default'):
            #作者列表
            list=response.xpath("//div[@class='main3']/div[@class='left']/div[@class='sonspic']/div[@class='cont']")
            name=list[0].xpath("//p[1]/a[1]/b/text()").extract()
            desc=list[0].xpath("//p[2]/text()").extract()
            poemlist=list[0].xpath("//p[2]/a/@href").extract()
            next=response.xpath("//div[@class='main3']/div[@class='left']/div[@class='pages']/a[last()]/@href").extract()
            # yield scrapy.Request(base_auther_url+next[0], callback=self.parse, dont_filter=True)
            #保存作者信息

            for poem in poemlist:
                yield scrapy.Request(base_url + poem, callback=self.parse, dont_filter=True)

        elif response.url.startswith('https://so.gushiwen.org/authors/authorvsw'):
             #作品列表
             plist = response.xpath("//div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']")
             title = plist[0].xpath("//p[1]/a[1]/b/text()").extract()
             time = plist[0].xpath("//p[2]/a[1]/text()").extract()
             poemist = plist[0].xpath("//p[2]/a[2]/text()").extract()
             content = plist[0].xpath("//div[2]/text()").extract()
             print(content)
             # print(title)




