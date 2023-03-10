# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PropertyItem(scrapy.Item):
    name = scrapy.Field()
    locality = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
