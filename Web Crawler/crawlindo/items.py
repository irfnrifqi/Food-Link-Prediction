# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndomaretItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nama_produk = scrapy.Field()
    komposisi   = scrapy.Field()
    pass
