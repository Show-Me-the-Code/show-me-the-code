# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from SugimotoYumi.items import SugimotoyumiItem


class YumiSpider(scrapy.Spider):
    name = "Yumi"
    allowed_domains = ["http://tieba.baidu.com/p/2166231880"]
    start_urls = ['http://tieba.baidu.com/p/2166231880?see_lz=1']

    def parse(self, response):
        item_loader = ItemLoader(item=SugimotoyumiItem(), response=response)
        item_loader.add_xpath("image_url", '//img[@class="BDE_Image"]/@src')
        yumi_item = item_loader.load_item()
        yield yumi_item




