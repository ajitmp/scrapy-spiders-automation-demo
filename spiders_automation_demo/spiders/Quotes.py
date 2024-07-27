import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css("div.quote")
        for quote in quotes:
            title=quote.css("span.text::text").get()
            author =quote.css("small.author::text").get()
            yield{
                'title':title,
                'author':author
            }
