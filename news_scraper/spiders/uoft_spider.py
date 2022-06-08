import scrapy


class UofTSpider(scrapy.Spider):
    name = "uoft"
    start_urls = ["https://www.utoronto.ca/news/searchnews/"]

    # We need to get all news docs

    def parse(self, response):
        pass
