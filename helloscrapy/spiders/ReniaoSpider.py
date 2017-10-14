# -*- coding: utf-8 -*-

import scrapy
from helloscrapy.items import ImageItem


class ReniaoSpider(scrapy.Spider):
    name = 'reniao'
    allowed_domains = ['www.53reniao.com']

    def start_requests(self):
        return [scrapy.Request("http://www.53reniao.com/logging.php?action=login", callback=self.__post_login)]

    def __post_login(self, response):
        post_data = {
            'username': 'sbno1',
            'password': 'sbno1',
        }
        return [scrapy.FormRequest.from_response(response, formdata=post_data, callback=self.__check_login_status)]

    def __check_login_status(self, response):
        # print(response.body.decode('gbk'))
        urls = [
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        base_url = 'http://www.o.com/'
        if response.url.startswith('http:/o.com/forum'):
            details = response.xpath("//a[@class='xst']/@href").extract()
            for d in details:
                new_url = base_url + d
                if not new_url.startswith("http://o.com/forum"):
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
