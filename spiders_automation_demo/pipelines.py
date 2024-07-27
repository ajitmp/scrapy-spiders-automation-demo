from scrapy.exceptions import DropItem

class FilterQuotesPipelineLoveOrLife:
    def process_item(self, item, spider):
        # Check if 'love' or 'life' is in the text
        if 'love' in item['title'].lower() or 'life' in item['title'].lower() or 'work' in item['title'].lower():
            return item
        else:
            raise DropItem(f"Quote without 'love' or 'life' or 'work' in title text: {item['title']}")

