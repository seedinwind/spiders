# -*- coding: utf-8 -*-

import scrapy
from scrapy.conf import settings
import json


# 爬取知乎问题
class ZhihuSpider(scrapy.Spider):
    name = 'zhihuquestion'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/api/v4/questions/66435486/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5', ]
    headers = settings['DEFAULT_REQUEST_HEADERS']
    headers.update({'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20', })  # 身份认证信息
    base_url = 'https://www.zhihu.com/question/'
    postfix = '/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5'

    def start_request(self):
        yield scrapy.Request(start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        url = response.url
        if url.startswith('https://www.zhihu.com/question'):
            # 解析知乎问题信息
            # item = ZhihuQuestionItem()
            # yield item
            pass
        elif url.startswith('https://www.zhihu.com/api'):
            result = json.loads(response.body_as_unicode())
            print(result)
            data = result['data']
            for d in data:
                id = d['url'].split("/")[-1]
                yield scrapy.Request(d['url'] + postfix, callback=self.parse, headers=self.headers)
                yield scrapy.Request(self.base_url + id, callback=self.parse, headers=self.headers)
