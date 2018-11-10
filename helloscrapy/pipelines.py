# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import urllib
import pymongo
import hashlib
from scrapy.conf import settings
from helloscrapy.items import PoemAuther,PoemInfo


class HelloscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


# class DownloadImagePipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):  # 下载图片
#             yield Request(item['imageurl'], dont_filter=True)  # 添加meta是为了下面重命名文件名使用
#
#     def file_path(self, request, response=None, info=None):
#         path=request.url.split("/")
#         filename = path[-2]+"/"+path[-3]+path[-1]
#         return filename

class PoemPipline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll_author = self.db[settings['COL_AUTHOR']]  # 获得collection的句柄
        self.coll_content = self.db[settings['COL_CONTENT']]  # 获得collection的句柄
        self.temp = dict()
    def process_item(self,item,spider):
        poem = dict(item)  # 把item转化成字典形式
        if isinstance(item,PoemAuther):
           self.coll_author.insert(poem)  # 向数据库插入一条记录
        elif isinstance(item,PoemInfo):
            md5= hashlib.md5(item["content"].encode('utf-8').strip()).hexdigest()
            if self.temp.has_key(md5):
               print("已存在")
            else:
               self.temp[md5] = md5
               self.coll_content.insert(poem)  # 向数据库插入一条记录