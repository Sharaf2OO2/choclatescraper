import scrapy
from choclatescraper.items import ChoclateProduct
from choclatescraper.itemloaders import ChoclateProductLoader
class ChoclatespiderSpider(scrapy.Spider):
    name = "choclatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        products = response.css('product-item')

        for product in products:
                        
            choclate = ChoclateProductLoader(item=ChoclateProduct(),selector=product)
            choclate.add_css('Name','a.product-item-meta__title::text')
            choclate.add_css('Price','span.price', re = '<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
            choclate.add_css('URL', 'a.product-item-meta__title::attr(href)')

            yield choclate.load_item()
        
        next_page = response.css('[rel="next"]::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url,self.parse)
