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

            detail_link = estate.xpath('../..//*[@class="details-link "]/@href').extract_first()
            detail_link = response.urljoin(detail_link)
            request = scrapy.Request(detail_link, callback=self.parse_details)
            

            print price, address, property_type, bed, bath, car, land_size, land_unit, detail_link

        next_page = response.xpath('//*[@class="pagination__next"]/a/@href').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    @staticmethod
    def parse_details(response):
        house = response.meta['item']
        primary_content = response.css("div#detailsCont #primaryContent")
        house['title'] = primary_content.css("p.title::text").extract_first()
        house['description'] = primary_content.css("p.body::text").extract()
        other_features = []
        features = response.css("div#detailsCont #primaryContent #features div.featureList").css("ul li")
        for li in features:
            other1 = OtherFeatures()
            other1['name'] = li.css("::text").extract_first()
            other1['description'] = li.css("span::text").extract_first()
            other_features.append(other1)

        house['otherFeatures'] = other_features
        yield house
