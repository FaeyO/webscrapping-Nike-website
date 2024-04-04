import scrapy
from selenium import webdriver
from scrapy.selector import Selector



class ClothesSpider(scrapy.Spider):
    name = "clothes"
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/w/mens-clothing-6ymx6znik1"]
    

    def __init__(self):
         driver = webdriver.Chrome()
         driver.get("https://www.nike.com/w/mens-clothing-6ymx6znik1")
         self.html = driver.page_source
         driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        nike_clothes = resp.xpath("//div[@class='product-grid__items css-hvew4t']/div")
        for nike in nike_clothes:
            #name = nike.xpath(".//a[@class='product-card__link-overlay']/text()").get()
            name = nike.xpath(".//div[@class='product-card__title']/text()").get()
            price = nike.xpath(".//div[@class='product-price__wrapper css-9xqpgk']/div/text()").get()
            category = nike.xpath(".//div[@class='product-card__subtitle']/text()").get()
            color = nike.xpath(".//div[@class='product-card__product-count']/text()").get()
            product_img = nike.xpath(".//div[@data-testid='wall-image-loader']/img/@src").get()
            product_url = nike.xpath(".//a[@class='product-card__img-link-overlay']/@href").get()

            # yield scrapy.Request(url=product_url, callback=self.parse_shoes, meta={'clothes_name':name,
            #                                                                 'clothes_price':price,'clothes_category':category,'clothes_color':color,'clothes_url':product_url})

    # def parse_shoes(self,response):
    #         name = response.request.meta['clothes_name']
    #         price = response.request.meta['clothes_price']
    #         category = response.request.meta['clothes_category']
    #         color = response.request.meta['clothes_color']
    #         product_url = response.request.meta['clothes_url']
    #         photo_link = response.xpath("//img[@class='css-viwop1 u-full-width u-full-height css-147n82m']/@src").getall()

            yield{'name': name,
                  'price': price,
                  'category':category,
                  'color': color,
                  'product_url':product_url,
                  'image_link':str(product_img)}
