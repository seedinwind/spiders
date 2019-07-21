# -*- coding: gbk -*-

import scrapy
from helloscrapy.items import Dzj
import chardet


digitMap = {"九":9,
            "八":8,
            "七":7,
            "六":6,
            "五":5,
            "四":4,
            "三":3,
            "二":2,
            "一":1,}


def getnum(params):
    print(params)
    param = params
    a = 0
    b = 0
    c = 0
    if len(param) < 0:
        return 0
    if "百".encode('utf-8') in param.encode('utf-8'):
        a = digitMap[param[param.index("百")-1]] * 100
    if "十".encode('utf-8') in param.encode('utf-8'):
        if param[param.index("十") - 1] == "第":
            b = 10
        else:
            b = digitMap[param[param.index("十") - 1]]*10
    try:
       c = digitMap[param[len(param)-1]]
    except Exception:
        c = 0
    return a+b+c


def getjinti(param):
    juan="卷"
    # print("-----------------------")
    print(param)
    if juan.encode('utf-8') in param.encode('utf-8'):
        return param[0: param.find(juan)]
    else:
        return param


def getjuanhao(param):
    juan = "卷"
    print(param)
    if juan.encode('utf-8') in param.encode('utf-8'):
        return getnum(param[param.find(juan) + 1: len(param)])
    else:
        return 0


def getBuming(param):
    if "·".encode('utf-8') in param.encode('utf-8'):
        return param[0: param.find("·")].replace("\r\n", "")
    elif "、".encode('utf-8') in param.encode('utf-8'):
        return param[0: param.find("、")].replace("\r\n", "")

class dzjSpider(scrapy.Spider):
    name = 'dzj'
    allowed_domains = ['www.qldzj.com']
    start_urls = [
        'http://www.qldzj.com/html/qldzj-ml.htm',
        # 'http://www.qldzj.com/htmljw/0001-59.htm'
        # 'https://so.gushiwen.org/authors/authorvsw_1abe13750637A1.aspx',
    ]

    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        base_url = 'http://www.qldzj.com/'
        if response.url.startswith('http://www.qldzj.com/html/qldzj-ml.htm'):
            print(response)
            p = response.xpath("//tr/td/a/@href").extract()
            for n in range(0,len(p)-1):
                new_url = p[n].replace('../',base_url,1)
                yield scrapy.Request(new_url, callback=self.parse, dont_filter=True)
        else:
            firstJWBox = response.xpath("//div[@class='jwbt-box'][1]")
            folling = response.xpath("//div[@class='jwbt-box'][1]/following-sibling::*")
            jw = ""
            yizhe = response.xpath("//div[@class='top-right'][1]/text()").extract()[0]
            buming = response.xpath("//div[@class='top-left'][1]/text()").extract()[0]
            jingti = firstJWBox.xpath("./div[@class='jwbt']/a[2]/text()").extract()[0]
            pinming = ""
            NoPin = 0
            NoJuan = 0
            for n in range(0, len(folling)-1):
                if folling[n].extract().startswith('<div'):
                    info = Dzj()
                    info['jingti'] = getjinti(jingti)
                    info['content'] = jw
                    info['pinming'] = pinming
                    info['buming'] = getBuming(buming)
                    info['juanhao'] = getjuanhao(jingti)
                    info['yizhe'] = yizhe
                    if info['juanhao'] != NoJuan:
                        NoPin = 0
                        NoJuan = info['juanhao']
                    info['pinhao'] = NoPin
                    bt = folling[n].xpath("./div[@class='jwbt']/a[2]/text()").extract()
                    btbm = folling[n].xpath("./div[@class='jwbtbm']/a[2]/text()").extract()
                    yield info
                    if len(btbm) > 0:
                        pinming = folling[n].xpath("./div[@class='jwbtbm']/a[2]/text()").extract()[0]
                    if len(bt) > 0:
                        jingti = bt[0]
                    jw = ""
                    NoPin += 1
                elif folling[n].extract().startswith('<p>'):
                    jwlist = folling[n].xpath("./text()").extract()
                    for n in range(0, len(jwlist)):
                        jw += jwlist[n].replace("\u3000\u3000", "")
            info = Dzj()
            info['jingti'] = getjinti(jingti)
            info['juanhao'] = getjuanhao(jingti)
            info['pinming'] = pinming
            info['buming'] = getBuming(buming)
            info['content'] = jw
            info['yizhe'] = yizhe
            if info['juanhao'] != NoJuan:
                NoPin = 0
            info['pinhao'] = NoPin
            yield info






