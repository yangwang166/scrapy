# -*- coding: utf-8 -*-
import scrapy


class MyschoolSpider(scrapy.Spider):
    name = 'myschool'
    allowed_domains = ['www.myschool.edu.au/school/50503']
    start_urls = ['http://www.myschool.edu.au/school/50503/']

    def parse(self, response):
      icsea_score = response.xpath('//*[@id="body-area"]/div[2]/section[1]/div[1]/ul/li[1]/div[2]/text()').extract()
      school_name = response.xpath('/html/body/div[1]/div/div[1]/div[1]/h1/text()').extract()

      yield {'School_Name': school_name, 'ICSEA_Score': icsea_score}
