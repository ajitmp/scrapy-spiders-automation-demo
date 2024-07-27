#spiders_automation_demo/itemsloader.py
#required imports
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst,MapCompose


#define your methods to apply on item value
def to_title_case(title):
    return title.title()


#define your loader class
class QuoteLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(str.strip, to_title_case)
    author_in = MapCompose(str.strip, to_title_case)
    


