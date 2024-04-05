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
        
        next_page = response.css('[rel="next"]::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url,self.parse)
