import scrapy
from selenium import webdriver
from scrapy.selector import Selector



class MenShoesSpider(scrapy.Spider):
    name = "men_shoes"
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/w/mens-clothing-6ymx6znik1"]
    #start_urls = ["https://www.nike.com/w/mens-shoes-nik1zy7ok"]

    def __init__(self):
         driver = webdriver.Chrome()
         #driver.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
         driver.get("https://www.nike.com/w/mens-clothing-6ymx6znik1")
         self.html = driver.page_source
         driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        men_shoes = resp.xpath("//div[@class='product-grid__items css-hvew4t']/div")
        for shoes in men_shoes:
            #name = shoes.xpath(".//a[@class='product-card__link-overlay']/text()").get()
            name = shoes.xpath(".//div[@class='product-card__title']/text()").get()
            price = shoes.xpath(".//div[@class='product-price__wrapper css-9xqpgk']/div/text()").get()
            category = shoes.xpath(".//div[@class='product-card__subtitle']/text()").get()
            color = shoes.xpath(".//div[@class='product-card__product-count']/text()").get()
            product_img = shoes.xpath(".//div[@data-testid='wall-image-loader']/img/@src").get()
            product_url = shoes.xpath(".//a[@class='product-card__img-link-overlay']/@href").get()

            # yield scrapy.Request(url=product_url, callback=self.parse_shoes, meta={'shoe_name':name,
            #                                                                 'shoe_price':price,'shoe_category':category,'shoe_color':color,'shoe_url':product_url})

    # def parse_shoes(self,response):
    #         name = response.request.meta['shoe_name']
    #         price = response.request.meta['shoe_price']
    #         category = response.request.meta['shoe_category']
    #         color = response.request.meta['shoe_color']
    #         product_url = response.request.meta['shoe_url']
    #         photo_link = response.xpath("//img[@class='css-viwop1 u-full-width u-full-height css-147n82m']/@src").getall()

            yield{'name': name,
                  'price': price,
                  'category':category,
                  'color': color,
                  'product_url':product_url,
                  'image_link':str(product_img)}
