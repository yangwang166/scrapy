# -*- coding: utf-8 -*-
import scrapy

class House(scrapy.Item):
    address = scrapy.Field()
    price = scrapy.Field()
    property_type = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    carPark = scrapy.Field()
    land_size = scrapy.Field()
    land_unit = scrapy.Field()
    detail_link = scrapy.Field()
    statement_url = scrapy.Field()

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.realestate.com.au']
    start_urls = ['https://www.realestate.com.au/buy/in-vic/list-1']

    def parse(self, response):
        for estate in response.xpath('//*[@class="residential-card__content"]'):

            house = House()

            price = estate.xpath('div[1]/span/text()').extract_first()
            house['price'] = price

            address = estate.xpath('div[2]/div/h2/a/span/text()').extract_first()
            house['address'] = address

            property_type = estate.xpath('div[2]/p/span/text()').extract_first()
            house['property_type'] = property_type

            feature_count = len(estate.xpath('div[3]/ul/li'))
            bed = 0
            bath = 0
            carPark = 0
            if feature_count > 0:
                bed = estate.xpath('div[3]/ul/li[1]/span[1]/text()')[1].extract()
                house['bed'] = bed 
            if feature_count > 1:
                bath = estate.xpath('div[3]/ul/li[2]/span[1]/text()')[1].extract()
                house['bath'] = bath
            if feature_count > 2:
                carPark = estate.xpath('div[3]/ul/li[3]/span[1]/text()')[1].extract()
                house['carPark'] = carPark

            land_count = len(estate.xpath('div[3]/div'))
            land_size = 0
            land_unit = None
            if land_count > 0:
                land_size = estate.xpath('div[3]/div/span/text()').extract()[1]
                house['land_size'] = land_size
                land_unit = estate.xpath('div[3]/div/span/text()').extract()[3]
                house['land_unit'] = land_unit

            detail_link = estate.xpath('../..//*[@class="details-link "]/@href').extract_first()
            detail_link = response.urljoin(detail_link)
            house['detail_link'] = detail_link
            request = scrapy.Request(detail_link, callback=self.parse_details)

            request.meta['item'] = house
            yield request
            
            #statement_url = house['statement_url']
            #print price, address, property_type, bed, bath, carPark, land_size, land_unit, detail_link

        next_page = response.xpath('//*[@class="pagination__next"]/a/@href').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    @staticmethod
    def parse_details(response):
        house = response.meta['item']
        statement_url = response.xpath('//*[@class="statement-of-information__link"]/@href').extract_first() 
        if statement_url != None:
            house['statement_url'] = statement_url
        yield house
