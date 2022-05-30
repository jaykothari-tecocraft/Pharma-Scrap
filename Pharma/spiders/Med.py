import scrapy
import requests
from bs4 import BeautifulSoup
from ..items import PharmaItem

class MedSpider(scrapy.Spider):
    name = 'Med'
    allowed_domains = ['mcareexports.com']
    start_urls = ['http://mcareexports.com/our-products/']
    page = 2
    
    def parse(self, response):
        items= PharmaItem()
        tags = response.css('span.nxowoo-box')

        for one in tags:
            title = one.css('h2.woocommerce-loop-product__title::text')[0].extract()
            img = one.css('a.woocommerce-LoopProduct-link img::attr(data-src)')[0].extract()
            # med_name = '-'.join(title.split())
            # url = f'https://mcareexports.com/our-products/{med_name}/'
            # res = requests.get(url)
            # mg = self.inside(res.text)
            items['name'] = title
            items['img'] =  img

            yield items

        if self.page < 849:
            next_url = f'https://mcareexports.com/our-products/page/{self.page}/'
            print(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Page : {self.page} <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

            self.page += 1
            yield response.follow(next_url,callback = self.parse)

    def inside(self,response):
        soup = BeautifulSoup(response,'html.parser')
        try:
            tag = soup.find("div",class_='woocommerce-product-details__short-description')
            p = tag.find_all('p')[-1]
            return p.text
        except:
            return None
        
