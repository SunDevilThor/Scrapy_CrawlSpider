# Scrapy CrawlSpider
# Tutorial from John Watson Rooney YouTube channel

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://sipwhiskey.com/collections/japanese-whisky
# https://sipwhiskey.com/collections/japanese-whisky/products/nikka-coffey-malt-whisky

class SipWhiskySpider(CrawlSpider):
    name = 'sip_whisky'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['https://sipwhiskey.com/']

    rules = (
        Rule(LinkExtractor(allow='collections/japanese-whisky', deny='products')),
        Rule(LinkExtractor(allow='products'), callback='parse_item'),
    )

    def parse_item(self, response):
        yield {
            'brand': response.css('div.vendor a::text').get(),
            'name': response.css('h1.title::text').get(),
            'price': response.css('span.price::text').get(),
        }

