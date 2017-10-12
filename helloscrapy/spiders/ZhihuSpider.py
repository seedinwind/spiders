# -*- coding: utf-8 -*-

import scrapy
from scrapy.conf import settings

# 爬取知乎问题
class ZhihuSpider(scrapy.Spider):
    name = 'zhihuquestion'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/api/v4/questions/66435486/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5', ]
    # cookies = {
    #     'd_c0': 'AICCtQPADguPTkVIbdfzabmLSW6RHwiraBA=|1482748420',
    #     '__utma': '51854390.1987020153.1482748431.1482748431.1482748431.1',
    #     '__utmv': '51854390.000 - - | 3 = entry_date = 20161225 = 1',
    #     'q_c1': '580d11edf06d40f1a88259e9eb29351b | 1502359598000 | 1482748420000',
    #     'aliyungf_tc': 'AQAAAE2mJAVTtwUAQykmapTTnmZUNZar',
    #     'q_c1': '580d11edf06d40f1a88259e9eb29351b | 1507789813000 | 1482748420000',
    #     '_xsrf': '05aaee6f - e619 - 4c3b - 9093 - 655995f41419',
    # }
    headers=settings['DEFAULT_REQUEST_HEADERS']
    headers.update({ 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',})

    def start_request(self):
        yield scrapy.Request(start_urls[0], callback=parse,headers=self.headers)

    def parse(self, response):
        print(response.body.decode('utf-8'))
