# -*- coding: gbk -*-

import scrapy
from helloscrapy.items import Gaoseng


class Gaosengzhuan(scrapy.Spider):
    name = 'gaoseng'
    allowed_domains = ['ctext.org']
    start_urls = [
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_01.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_02.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_03.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_04.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_05.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_06.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_07.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_08.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_09.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_10.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_11.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_12.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_13.htm',
        'http://www.ldbj.com/gaosengzhuan/lianggaosengzhuan_14.htm'
        # 'https://so.gushiwen.org/authors/authorvsw_1abe13750637A1.aspx',
    ]

    def start_request(self):
        for url in start_urls:
           yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
             p=response.xpath("//div[@class='zhengwen']/div[@class='mid']/p")
             content=p[3].xpath("//text()").extract()
             concat=""
             for n in range(0,len(content)-1):
                 concat+=content[n].encode("utf-8")
             info=Gaoseng()
             info['content']=concat
             yield  info

