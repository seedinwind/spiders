# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imageurl = scrapy.Field()


class ZhihuQuestionItem(scrapy.Item):
     name=scrapy.Field()

class PoemAuther(scrapy.Item):
     name = scrapy.Field()
     desc = scrapy.Field()

class PoemInfo(scrapy.Item):
     title = scrapy.Field()
     time = scrapy.Field()
     author = scrapy.Field()
     content = scrapy.Field()
     md5 =scrapy.Field()

class Gaoseng(scrapy.Item):
     title = scrapy.Field()
     content = scrapy.Field()


class Dzj(scrapy.Item):
      buming=scrapy.Field()
      jingti=scrapy.Field()
      pinming = scrapy.Field()
      content = scrapy.Field()
      yizhe = scrapy.Field()
      pinhao = scrapy.Field() #经文品编号  卷内编号
      juanhao = scrapy.Field() #经文卷编号
