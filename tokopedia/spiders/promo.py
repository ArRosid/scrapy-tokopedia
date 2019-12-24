# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PromoSpider(CrawlSpider):
    name = 'promo'
    allowed_domains = ['tokopedia.com']
    start_urls = ['https://tokopedia.com/promo']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='promotion-cta']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['description'] = response.xpath("normalize-space(//h1[@class='post-content__title']/text())").get()
        item['periode'] = response.xpath("normalize-space(//div[@class='postbox-content-detail postbox-content--period']/p[@class='postbox-content__p'][1]/text())").get()
        item['minimum_transaction'] = response.xpath("normalize-space(//div[@class='postbox-content-detail postbox-content--min-transaction']/p[@class='postbox-content__p'][1]/text())").get()
        item['promo_code'] = response.xpath("//input[@class='postbox-content-voucher__input'][1]/@value").get()
        return item
