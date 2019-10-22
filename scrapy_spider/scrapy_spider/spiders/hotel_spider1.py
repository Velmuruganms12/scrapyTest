# -*- coding: utf-8 -*-
import scrapy


class HotelSpider1Spider(scrapy.Spider):
    name = 'hotel_spider1'
    allowed_domains = ['https://www.panpacific.com/en/hotels-and-resorts.html']
    start_urls = ['https://www.panpacific.com/en/hotels-and-resorts.html']

    def parse(self, response):
        sel = scrapy.Selector(response)
        itemlist = []
        posts = sel.xpath("//*[@class='row']")
        post21 = posts.xpath("div[@class='row']")
        print("-6666--", post21)
        for post in posts:
            print("-88888--", post)
            post22 = post.xpath('a/@href').extract()
            print("-88888--", post22)
            #for post41 in post22:
                #print(" ++++++  1111 ", posts4)
                #posts6 = posts4.select("div[@class='hotel-resort-item']")
                #print(" ++++++ ", posts31)
        #print("----", posts)

        #posts  = response.xpath("//div[@class='hotel-resort-item']//a/@href").extract()
        yield {'quotes': itemlist}