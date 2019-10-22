# -*- coding: utf-8 -*-
import scrapy


class HotelSpider2Spider(scrapy.Spider):
    name = 'hotel_spider2'
    allowed_domains = ['https://www.panpacific.com/en/hotels-and-resorts.html']
    start_urls = ['https://www.panpacific.com/en/hotels-and-resorts.html/']

    def parse(self, response):
        sel = scrapy.Selector(response)
        itemlist = []
        posts = response.xpath('//div[@data-endpoint != ""]')
        for post in posts:
            posts2 = post.xpath("//div[@class='col-12.col-md-6.col-sm-6']")
            print("-88888--", posts2)
            posts4 = posts2.xpath("//*[@class='col-12.col-md-6.col-sm-6']")
            print(" ++++++ ", posts4)
            for post41 in posts4:
                #print(" +++post41+++ " , post41)
                posts31 = post41.select("div[@class='hotel-resort-item']")
                #posts6 = posts4.select("div[@class='hotel-resort-item']")
                print(" ++++++ ", posts31)
            for post5 in posts31:
                posts7 = post5.select("div[@class='hotel-resort-item']")
                print("----", posts7)
                itemlist.append(posts7)
        #print("----", posts)

        #posts  = response.xpath("//div[@class='hotel-resort-item']//a/@href").extract()
        yield {'quotes': itemlist}
