# -*- coding: utf-8 -*-
import scrapy

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.realestate.com.au']
    start_urls = ['https://www.realestate.com.au/buy/in-wa/list-1']

    def parse(self, response):
        for estate in response.xpath('//*[@class="residential-card__content"]'):

            price = estate.xpath('div[1]/span/text()').extract_first()

            address = estate.xpath('div[2]/div/h2/a/span/text()').extract_first()
            property_type = estate.xpath('div[2]/p/span/text()').extract_first()

            feature_count = len(estate.xpath('div[3]/ul/li'))
            bed = 0
            bath = 0
            car = 0
            if feature_count > 0:
                bed = estate.xpath('div[3]/ul/li[1]/span[1]/text()')[1].extract()
            if feature_count > 1:
                bath = estate.xpath('div[3]/ul/li[2]/span[1]/text()')[1].extract()
            if feature_count > 2:
                car = estate.xpath('div[3]/ul/li[3]/span[1]/text()')[1].extract()

            land_count = len(estate.xpath('div[3]/div'))
            land_size = 0
            land_unit = None
            if land_count > 0:
                land_size = estate.xpath('div[3]/div/span/text()').extract()[1]
                land_unit = estate.xpath('div[3]/div/span/text()').extract()[3]
            

            print price, address, property_type, bed, bath, car, land_size, land_unit

        next_page = response.xpath('//*[@class="pagination__next"]/a/@href').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

