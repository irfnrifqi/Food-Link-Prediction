import scrapy
from ..items import Halal2Item
from urllib.parse import urljoin

class crawlhalal2(scrapy.Spider):
    name = 'halal2'
    page_number = 2
    start_urls = [
        'https://www.halalmui.org/mui14/searchproduk/search/detailgroupkategori/?groupcode=27'
        ]
       
    def parse(self, response):
        items = Halal2Item()
        nama_produk1 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[1]/td/a").extract()
        nama_produk2 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[2]/td/a").extract() 
        nama_produk3 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[3]/td/a").extract() 
        nama_produk4 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[4]/td/a").extract() 
        nama_produk5 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[5]/td/a").extract() 
        nama_produk6 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[6]/td/a").extract() 
        nama_produk7 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[7]/td/a").extract() 
        nama_produk8 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[8]/td/a").extract() 
        nama_produk9 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[9]/td/a").extract()  
        nama_produk10 = response.xpath("/html/body/div[6]/div/div/div[2]/table/tbody/tr[10]/td/a").extract()   
        items['nama_produk1'] = nama_produk1
        items['nama_produk1'] = nama_produk2
        items['nama_produk1'] = nama_produk3
        items['nama_produk1'] = nama_produk4
        items['nama_produk1'] = nama_produk5
        items['nama_produk1'] = nama_produk6
        items['nama_produk1'] = nama_produk7
        items['nama_produk1'] = nama_produk8
        items['nama_produk1'] = nama_produk9
        items['nama_produk1'] = nama_produk10
        yield items

        next_page = 'https://www.halalmui.org/mui14/searchproduk/search/detailgroupkategori/?groupcode=27&page=' + str(crawlhalal2.page_number) 
        if crawlhalal2.page_number < 324:
             crawlhalal2.page_number += 1
             yield response.follow(next_page, callback = self.parse)
        
 # kategori: .table-cph-btn /html/body/div[6]/div/div/div[2]/table/tbody/tr[1]/td/a
 # web kategori: https://www.halalmui.org/mui14/searchproduk/search/detailgroupkategori/?groupcode=15&page=1
 # url produk: response.css('#detail::attr(href)').extract_first()
#16-2548-beverage
#17-135-gel
#18-828-oil
 
