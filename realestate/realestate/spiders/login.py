# -*- coding: utf-8 -*-
import scrapy
import requests
import re

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

dbf = open("/home/willwywang/scrapy/project/realestate/db.csv", "a+")

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.realestate.com.au']
    #start_urls = ['https://www.realestate.com.au/buy/in-vic/list-1']
    start_urls = [
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3129/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3002/list-1?includeSurrounding=false'
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3039/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3040/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3041/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3044/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3046/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3053/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3055/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3056/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3057/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3058/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3060/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3065/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3066/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3067/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3068/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3070/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3071/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3072/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3073/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3078/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3079/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3081/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3083/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3084/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3101/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3102/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3103/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3104/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3108/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3109/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3111/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3121/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3122/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3123/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3124/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3125/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3126/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3127/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3128/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3129/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3130/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3131/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3132/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3133/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3134/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3141/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3142/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3143/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3144/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3145/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3146/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3147/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3148/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3149/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3150/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3151/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3161/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3162/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3163/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3165/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3166/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3167/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3168/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3181/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3182/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3184/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3185/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3186/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3187/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3188/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3189/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3192/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3193/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3194/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3202/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3204/list-1?includeSurrounding=false',
                 'https://www.realestate.com.au/buy/property-house-with-2-bedrooms-between-500000-15000000-in-3206/list-1?includeSurrounding=false'
                 ]

    def parse(self, response):
        #count = 0 
        for estate in response.xpath('//*[@class="residential-card__content"]'):
            #count += 1

            house = House()

            house['land_size'] = "null"
            house['address'] = "null"
            house['price'] = 0
            house['bed'] = 0
            house['bed'] = 0
            house['carPark'] = 0
            house['land_unit'] = "null"
            house['detail_link'] = "null"
            house['statement_url'] = "null"

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
            land_size = "null"
            land_unit = None
            if land_count > 0:
                land_size = estate.xpath('div[3]/div/span/text()').extract()[1]
                house['land_size'] = land_size
                land_unit = estate.xpath('div[3]/div/span/text()').extract()[3]
                house['land_unit'] = land_unit

            detail_link = estate.xpath('../..//*[@class="details-link "]/@href').extract_first()
            detail_link = response.urljoin(detail_link)
            house['detail_link'] = detail_link

            req = scrapy.Request(detail_link, 
                                    callback=self.parse_details)

            req.meta['item'] = house
            yield req
            
            #statement_url = house['statement_url']
            #print count, price, address, property_type, bed, bath, carPark, land_size, land_unit, detail_link

        next_page = response.xpath('//*[@class="pagination__next"]/a/@href').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, 
                                callback=self.parse)

    def parse_details(self, response):
        house = response.meta['item']
        statement_url = response.xpath('//*[@class="statement-of-information__link"]/@href').extract_first() 


        if statement_url != None:
            house['statement_url'] = statement_url

            #yield scrapy.Request(
            #    statement_url,
            #    callback=self.save_pdf)

            resp = requests.get(statement_url, stream=True)
            file_name = re.sub(r'\W+', '', house['address']+'_'+house['property_type']+'_'+str(house['bed'])+'_'+str(house['bath'])+'_'+str(house['carPark']))
            path = '/home/willwywang/statement_pdf/' + file_name + '.pdf'
            with open(path, 'wb') as fd:
                fd.write(resp.content)
            
            if house['land_size'] is None:
                house['land_size'] = "null"
            if house['address'] is None:
                house['address'] = "null"
            if house['price'] is None:
                house['price'] = 0
            if house['bed'] is None:
                house['bed'] = 0
            if house['bath'] is None:
                house['bed'] = 0
            if house['carPark'] is None:
                house['carPark'] = 0
            if house['land_unit'] is None:
                house['land_unit'] = "null"
            if house['detail_link'] is None:
                house['detail_link'] = "null"
            if house['statement_url'] is None:
                house['statement_url'] = "null"

            address_new = house['address'].replace(",", " ")
            price_new = house['price'].replace(",", "")
            land_size_new = house['land_size'].replace(",", "")

            aline = u'' + address_new + ',' + price_new + ',' + house['property_type'] + ',' + str(house['bed']) + ',' + str(house['bath']) + ',' + str(house['carPark']) + ',' + land_size_new + ',' + house['land_unit'] + ',' + house['detail_link'] + ',' + house['statement_url'] + ',' + file_name
            aline = aline.encode('utf-8').strip()
            dbf.write(aline + "\n")
            dbf.flush()

        yield house

    #def save_pdf(self, response):
    #    print "Downloading pdf..."
    #    house = response.meta['item']
    #    path = '/tmp/' + house['address'] + '.pdf'
    #    print path
    #    with open(path, 'wb') as f:
    #        f.write(response.body)
