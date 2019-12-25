# -*- coding: utf-8 -*-
import scrapy


class Best10RoboticBooksSpider(scrapy.Spider):
    name = 'best_10_robotic_books'
    allowed_domains = ['www.tokopedia.com']
    start_urls = ['https://www.tokopedia.com/p/buku/teknik-sains/buku-robotika?ob=5']

    def parse(self, response):
        item = 0
        books = response.xpath("//div[@class='css-bk6tzz e1nlzfl3']/a")
        for book in books:
            if item == 10: #If already 10 books
                break

            book_title = book.xpath(".//div[2]/div[2]/span[1]/text()").get()
            book_price = book.xpath(".//div[2]/div[2]/div/div/span/text()").get()
            seller_location = book.xpath(".//div[2]/div[2]/div[2]/div/span[1]/text()").get()

            for _ in range(5,0,-1): #looping from 5 to 1
                rating = book.xpath(f".//div[2]/div[2]/div[3]/div/img[{_}]/@src").get()
                rating = rating.split("/")
                if rating[-1] == "4fede911.svg": #if the star is yellow
                    rating = _
                    break


            rating_count = book.xpath(".//div[2]/div[2]/div[3]/div/span/text()[2]").get()
            
            item = item + 1

            yield {
                "book_title": book_title,
                "book_price": book_price,
                "seller_location": seller_location,
                "rating": rating,
                "rating_count": rating_count,
            }
