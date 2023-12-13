import scrapy


class PepParseItem(scrapy.Item):
    """Добыча паука"""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
