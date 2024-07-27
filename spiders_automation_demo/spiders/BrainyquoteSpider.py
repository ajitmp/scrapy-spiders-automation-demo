import scrapy
from spiders_automation_demo.items import QuoteItem
from spiders_automation_demo.itemsloader import QuoteLoader

class BrainyquoteSpider(scrapy.Spider):
    name = "BrainyQuote"
    allowed_domains = ["www.brainyquote.com"]
    start_urls = ['https://www.brainyquote.com/topics/life-quotes']

    def parse(self, response):
        #each quote is within <div class="quote" ...>
        quotes = response.css("div.grid-item.qb.clearfix.bqQt")
        for quote in quotes:
            #create your item object
            #quote_item = QuoteItem()
            #create your loader
            loader = QuoteLoader(item=QuoteItem(), selector=quote)
            #add your selector to your item
            #each quote text is within <span class="text" ...>
            loader.add_css('title',"div::text")
            #each author info is within <small class="author" ...>
            loader.add_css('author',"a.bq-aut.qa_109542.oncl_a::text")  

            #yield your item via the loader using .load_item()
            yield loader.load_item()