import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        #each quote is within <div class="quote" ...>
        quotes = response.css("div.quote")
        for quote in quotes:
            #each quote text is within <span class="text" ...>
            title=quote.css("span.text::text").get()
            #each author info is within <small class="author" ...>
            author =quote.css("small.author::text").get()
            yield{
                'title':title,
                'author':author
            }
