import scrapy
from scrapy.selector import Selector


class ScraptutorSpider(scrapy.Spider):
    name = 'scraptutor'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1:5000/']

    def parse(self, response):
        data={
            'username':'user',
            'password':'user123'
        }

        return scrapy.FormRequest(
            url='http://127.0.0.1:5000/login',
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):

        ###2 task
        #1ambil semua data dibawa ke detail (parsing detail)
        #.ambil semua link di next, balik lagi(looping) ke after_login
        ###
        detail_product: list[Selector] = response.css('.card .card-title a')
        for  detail in detail_product: # diloop untuk detail produk
            href = detail.attrib.get('href')
            yield response.follow(href, callback=self.parse_detail)

        paginations: list[Selector] = response.css('.pagination a.page-link')
        for pagination in paginations:
            href = pagination.attrib.get('href')
            yield response.follow(href, callback=self.after_login)

    def parse_detail(self, response):
        image = response.css('.img-fluid').attrib.get('src')
        title = response.css('.card-title::text').get()
        price = response.css('.card-price::text').get()
        category = response.css('.card-category::text').get().replace('category: ','')
        description = response.css('.card-text::text').get()

        return{
            'image':image,
            'title':title,
            'price':price,
            'category':category,
            'description':description
        }

        #yield{'title':response.css['title'].get_text}

#response.css('title::text').get()
#response.css['title'].get_text