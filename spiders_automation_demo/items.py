#spiders_automation_demo/items.py
import scrapy

class QuoteItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()


