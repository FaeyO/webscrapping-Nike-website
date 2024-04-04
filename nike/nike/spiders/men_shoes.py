import scrapy
from selenium import webdriver
from scrapy.selector import Selector

class MenShoesSpider(scrapy.Spider):
    name = "men_shoes"
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/w/mens-shoes-nik1zy7ok"]

    def start_requests(self):
        driver = webdriver.Chrome()
        driver.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
        self.html = driver.page_source
        driver.close()
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        resp = Selector(text=self.html)
        men_shoes = resp.xpath("//div[@class='product-grid__items css-hvew4t']/div")
        for shoes in men_shoes:
            name = shoes.xpath(".//div[@class='product-card__title']/text()").get()
            price = shoes.xpath(".//div[@class='product-price__wrapper css-9xqpgk']/div/text()").get()
            category = shoes.xpath(".//div[@class='product-card__subtitle']/text()").get()
            color = shoes.xpath(".//div[@class='product-card__product-count']/text()").get()
            product_img = shoes.xpath(".//div[@data-testid='wall-image-loader']/img/@src").get()
            product_url = shoes.xpath(".//a[@class='product-card__img-link-overlay']/@href").get()

            yield {
                'name': name,
                'price': price,
                'category': category,
                'color': color,
                'product_url': product_url,
                'image_link': str(product_img)
            }
