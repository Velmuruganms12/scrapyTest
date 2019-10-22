# -*- coding: utf-8 -*-
import scrapy


class HotelTestSpider(scrapy.Spider):
    name = 'hotel_test'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
        yield {'quotes': quotes}
