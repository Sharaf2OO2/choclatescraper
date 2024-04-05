import scrapy


class ChoclatespiderSpider(scrapy.Spider):
    name = "choclatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://chocolate.co.uk"]

    def parse(self, response):
        pass
