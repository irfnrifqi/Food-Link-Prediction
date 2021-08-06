import scrapy
from ..items import IndomaretItem
from urllib.parse import urljoin

class crawlindomaret(scrapy.Spider):
    name = 'indomaret'
    page_number = 2
    start_urls = [
        'https://www.klikindomaret.com/category/minuman-tradisional'
        ]
    base_url = 'https://www.klikindomaret.com/'
       
    def parse(self, response):
        indomaret = response.xpath("//*[contains(@class, 'item')]/a/@href").extract()
        for i in indomaret:
            url = urljoin(response.url, i)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        for info in response.css('.produk-detail'):
            item = IndomaretItem()

            nama_produk   = info.css('h3.desktop-xs::text').extract_first(),
            komposisi     = info.css('.spec_id_KOMPOSISI::text').get(),
               
            item['nama_produk'] = nama_produk   
            item['komposisi'] = komposisi  
            
            yield item

        next_page = 'https://www.klikindomaret.com/category/cemilan--biskuit?categories=&sortcol=PROMO&page=' + str(crawlindomaret.page_number) + '&pagesize=50&attributes=&productbrandid=&startprice=&endprice='
        if crawlindomaret.page_number < 3:
             crawlindomaret.page_number += 1
             yield response.follow(next_page, callback = self.parse)
   
