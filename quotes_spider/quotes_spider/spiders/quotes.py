# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

class QuotesSpider(Spider):

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()

        yield FormRequest('http://quotes.toscrape.com/login', 
                          formdata = {'csrf_token': csrf_token,
                                      'username': 'foobar',
                                      'password': 'foobar'},
                          callback = self.scrape_home_page)

    def scrape_home_page(self, response):
        print response.xpath('//*')
        #if response.xpath('//a[text()="Logout"]'):
        #    self.log('You logged in!')

        #l = ItemLoader(item = QuotesSpiderItem(), response = response)

        #h1_tag = response.xpath('//h1/a/text()').extract_first()
        #tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        #l.add_value('h1_tag', h1_tag)
        #l.add_value('tags', tags)

        #return l.load_item()

        #yield {'H1 Tag': h1_tag, 'Tags': tags}

        #quotes = response.xpath('//*[@class="quote"]')
        #for quote in quotes:
        #  text = quote.xpath('.//*[@class="text"]/text()').extract_first() 
        #  author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        #  tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

        #  yield{'Text': text,
        #        'Author': author,
        #        'Tags': tags}

        #  next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()

        #  absolute_next_page_url = response.urljoin(next_page_url)

        #  yield Request(absolute_next_page_url)
