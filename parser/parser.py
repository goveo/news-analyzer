# scrapy runspider ...
import scrapy
import datetime
import os, sys

module_path = os.path.abspath(os.getcwd())

if module_path not in sys.path:
    sys.path.append(module_path)
from database import database


class Spider(scrapy.Spider):
    print("news parser")
    db = database.connect()
    name = 'news'
    allowed_domains = ['fakty.ua']
    page = 1
    base_url = "https://fakty.ua"
    url = 'https://fakty.ua/news?newswidget-main2_page='
    start_urls = ["{}{}".format(url, page)]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        print('parse')
        news = response.css('div.news-block')
        for item in news:
            title = item.xpath(".//h2//text()").extract_first()
            if title is not None:
                text = item.xpath(".//p//text()").extract_first()
                link = item.xpath(".//a//@href").extract_first()
                link = "{}{}".format(self.base_url, link)
                time = item.xpath(".//span[@class='time']//text()").extract_first()
                date = item.xpath(".//span[@class='g-gate']/text()").extract()[2]
                if (date == "сегодня"):
                    date = datetime.datetime.today()
                else:
                    date = datetime.datetime.strptime(date, '%d.%m.%Y')
                hour = int(time.split(":")[0])
                minute = int(time.split(":")[1])
                date = date.replace(hour=hour, minute=minute)
                # print(title)
                # print(text)
                # print(link)
                # print(date)
                self.db["news"].insert_one({
                    "title": title,
                    "text": text,
                    "link": link,
                    "date": date
                })

        self.page += 1

        print("parsing page : ", self.page)
        link = self.get_link()
        print("link : ", link)
        yield response.follow(link, self.parse)

    def get_link(self):
        return "{}{}".format(self.url, self.page)