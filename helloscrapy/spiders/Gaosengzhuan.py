# -*- coding: gbk -*-

import scrapy

class Gaosengzhuan(scrapy.Spider):
    name = 'gaoseng'
    allowed_domains = ['ctext.org']
    start_urls = [
        'http://www.lianhua33.com/gsz/gsz1.htm',
        'http://www.lianhua33.com/gsz/gsz2.htm',
        'http://www.lianhua33.com/gsz/gsz3.htm',
        'http://www.lianhua33.com/gsz/gsz4.htm',
        'http://www.lianhua33.com/gsz/gsz5.htm',
        'http://www.lianhua33.com/gsz/gsz6.htm',
        'http://www.lianhua33.com/gsz/gsz7.htm',
        'http://www.lianhua33.com/gsz/gsz8.htm',
        'http://www.lianhua33.com/gsz/gsz9.htm',
        'http://www.lianhua33.com/gsz/gsz10.htm',
        'http://www.lianhua33.com/gsz/gsz11.htm',
        'http://www.lianhua33.com/gsz/gsz12.htm',
        'http://www.lianhua33.com/gsz/gsz13.htm',
        'http://www.lianhua33.com/gsz/gsz14.htm',
        'http://www.lianhua33.com/gsz/gsz15.htm',
        'http://www.lianhua33.com/gsz/gsz16.htm'
        # 'https://so.gushiwen.org/authors/authorvsw_1abe13750637A1.aspx',
    ]

    def start_request(self):
        for url in start_urls:
           yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
             column=response.xpath("//p[@class='style4']/strong/text()").extract()
             content = response.xpath("//p[@class='style4']/text()").extract()
             concat = ""
             for n in range(0,len(content)-1):
                 concat
                 concat += content[n]
             print(column[0].encode("utf-8"))
             print(concat.encode("utf-8"))


