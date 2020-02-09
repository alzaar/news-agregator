import scrapy

class Crawler(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for q in response.css('div.quote'):
            yield {
                'text': q.css('span.text::text').get(),
                'author': q.xpath('span/small/text()').get(),
            }

            next_page = response.css('li.next a::attr("href")').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)