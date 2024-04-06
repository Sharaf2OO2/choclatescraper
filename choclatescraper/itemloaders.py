from email.policy import default
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class ChoclateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()
    Price_in = MapCompose(lambda x : x.split('£')[-1])
    URL_in = MapCompose(lambda x : 'https://www.chocolate.co.uk' + x)