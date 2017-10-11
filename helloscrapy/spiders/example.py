# -*- coding: utf-8 -*-

import scrapy
from helloscrapy.items import ImageItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.53reniao.com']
    start_urls = [
         'http://www.53reniao.com/forum-35-1.html'
    ]




    def parse(self, response):
        base_url = 'http://www.53reniao.com/'
        if response.url.startswith('http://www.53reniao.com/forum'):
            details = response.xpath("//a[@class='xst']/@href").extract()
            for d in details:
                new_url = base_url + d
                if not new_url.startswith("http://www.53reniao.com/forum"):
                    yield scrapy.Request(new_url, callback=self.parse, dont_filter=True)
        else:
            title = response.xpath("//head/title").extract()
            wrap = response.xpath("//div[@id='wrap']/div[@id='postlist']")
            defaultpost = wrap.xpath("//td[@class='postcontent']/div[@class='defaultpost']")
            postattachlist = defaultpost.xpath("//div[@class='postattachlist']")
            attachimage = postattachlist.xpath("//img/@file").extract()
            # for img in attachimage:
            #     print (img)
            t_msgfont = defaultpost.xpath("//td[@class='t_msgfont']")
            images = t_msgfont.xpath("//img/@src").extract()
            images.extend(attachimage)
            filter_images = [el for el in images if el.startswith("http") and (not 'avatar' in el)]
            if len(filter_images):
                print (title[0])
                for img in filter_images:
                    item = ImageItem()
                    item['imageurl'] = img
                    yield item
            else:
                print (title[0] + "未获取到图片-----------------")
