import scrapy


class IrctcSpider(scrapy.Spider):
    name = "irctc"
    allowed_domains = ["irctc.co.in"]
    start_urls = ["https://irctc.co.in"]

    def parse(self, response):
        pass
