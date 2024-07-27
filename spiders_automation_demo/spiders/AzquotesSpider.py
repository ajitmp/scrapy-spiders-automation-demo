import scrapy
from spiders_automation_demo.items import QuoteItem
from spiders_automation_demo.itemsloader import QuoteLoader

class AzquotesSpider(scrapy.Spider):
    name = "AzQuotes"
    allowed_domains = ["www.azquotes.com"]
    start_urls = ['https://www.azquotes.com/quotes/topics/life.html']

    def parse(self, response):
        #each quote is within <div class="quote" ...>
        quotes = response.css("div.wrap-block")
        for quote in quotes:
            #create your item object
            #quote_item = QuoteItem()
            #create your loader
            loader = QuoteLoader(item=QuoteItem(), selector=quote)
            #add your selector to your item
            #each quote text is within <span class="text" ...>
            loader.add_css('title',"p a.title::text")
            #each author info is within <small class="author" ...>
            loader.add_css('author',"div.author a::text")  

            #yield your item via the loader using .load_item()
            yield loader.load_item()