# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import urllib


class HelloscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class DownloadImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):  # 下载图片
            yield Request(item['imageurl'], dont_filter=True)  # 添加meta是为了下面重命名文件名使用

    def file_path(self, request, response=None, info=None):
        path=request.url.split("/")
        filename = path[-2]+"/"+path[-3]+path[-1]
        return filename
