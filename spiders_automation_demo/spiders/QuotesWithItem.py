import scrapy
from spiders_automation_demo.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "QuotesWithItem"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        #each quote is within <div class="quote" ...>
        quotes = response.css("div.quote")
        for quote in quotes:
            #create your item object
            quote_item = QuoteItem()
            #each quote text is within <span class="text" ...>
            title=quote.css("span.text::text").get()
            #each author info is within <small class="author" ...>
            author =quote.css("small.author::text").get()

            #add your selector to your item

            quote_item['title']=title
            quote_item['author']= author
            #yield your item
            yield quote_item