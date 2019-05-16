# -*- coding: utf-8 -*-
import scrapy
import re

#scrapy runspider ...


class Spider(scrapy.Spider):
    print("news parser")
    name = 'news'
    allowed_domains = ['fakty.ua']
    page = 1
    url = 'https://fakty.ua/news?newswidget-main2_page='
    start_urls = ["{}{}".format(url, page)]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        print('parse')
        news = response.css('div.news-block')
        counter = 0
        for item in news:
            print(counter)
            title = item.xpath(".//h2//text()").extract_first()
            if title is not None:
                text = item.xpath(".//p//text()").extract_first()
                link = item.xpath(".//a//@href").extract_first()
                time = item.xpath(".//span[@class='time']//text()").extract_first()
                date = item.xpath(".//span[@class='g-gate']/text()").extract()[2]



                print(title)
                print(text)
                print(link)
                print(time)
                print(date)
                counter += 1

        self.page += 1

        print("parsing page : ", self.page)
        link = self.get_link()
        print("link : ", link)
        yield response.follow(link, self.parse)

    def get_link(self):
        return "{}{}".format(self.url, self.page)