import scrapy


class ChoclatespiderSpider(scrapy.Spider):
    name = "choclatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        products = response.css('product-item')
        for product in products:
            yield{
                'Name': product.css('a.product-item-meta__title::text').get(),
                'Price': product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
                'URL':  product.css('a.product-item-meta__title').attrib['href']
            }
