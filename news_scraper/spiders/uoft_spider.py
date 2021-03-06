import scrapy


class UofTSpider(scrapy.Spider):
    name = "uoft"
    start_urls = ["https://www.utoronto.ca/news/searchnews/"]

    def parse(self, response):
        content = response.css("div.view-content")
        news_articles = content.css("div.panel-col-last")
        news_article_links = news_articles.css(
            "h4.field-content a::attr(href)")
        yield from response.follow_all(news_article_links, self.parse_news_doc)

        pagination_link = response.css("li.pager-next a")
        yield from response.follow_all(pagination_link, self.parse)

    # Function for parsing each news document separately
    def parse_news_doc(self, response):
        def clean_text(query):
            text_list = response.css(query).getall()
            text = (' ').join(text_list)
            text = text.replace('\xa0', '')
            return text.strip()

        yield {
            "Name": response.css("div.pane-content h1::text").get().strip(),
            "Date": response.css("div.date::text").get(),
            "Content": clean_text("div.row div.pane-content p::text, strong::text"),
            "Tags": response.css("div.Tags div.pane-content a::text").getall()
        }
