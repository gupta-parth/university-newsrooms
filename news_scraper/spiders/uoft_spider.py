import scrapy


class UofTSpider(scrapy.Spider):
    name = "uoft"
    start_urls = ["https://www.utoronto.ca/news/searchnews/"]

    # We need to get all news docs
    def parse(self, response):
        content = response.css("div.view-content")
        news_articles = content.css("div.panel-col-last")

        for article in news_articles:
            yield {
                "name": article.css("h4.field-content a::text").get()
            }
