# scrapping_with_scrapy

pip install scrapy

bila perlu update c++ build tools :
https://visualstudio.microsoft.com/visual-cpp-build-tools/

DEPRECATION: Twisted was installed using the legacy 'setup.py install' method, because a wheel could not be built for it.
 pip 21.0 will remove support for this functionality. A possible replacement is to fix the wheel build issue reported above
. You can find discussion regarding this at https://github.com/pypa/pip/issues/8368.

scrapy startproject <namaproyek>

akan membuat foler nama proyek beserta file2 proyek scrapy

cd namaproyek
scrapy genspider <namaproyekspiders> <alamat web - tanpa http>

jalankan spiders

scrapy crawl <namaproyekspiders>

yield {'':'', '':'','':''}

yield membuat dictionary 

bikin data untuk username dan password

return scrapy.formrequest

untuk cek kebutuhan formrequest crtk+shift+i

ctrl+klik untuk cek yang lain

untu data

    def parse(self, response):
        data={
            'Username':'user',
            'Password':'user123'
        }
hasil gagal login. mesti huruf kecil

    def parse(self, response):
        data={
            'username':'user',
            'password':'user123'
        }
        


membedakan

response.css('.card .card-title a')  dan
response.css('.pagination a.page-link') 

class didahului . , a tidak didahului titik 


jadi file csv 

scrapy crawl scraptutor -o data.csv
scrapy crawl scraptutor -o data.json
   
   
       def parse_detail(self, response):
           image = response.css('.img-fluid').attrib.get('src')
           title = response.css('.card-title::text').get()
           price = response.css('.card-price::text').get()
           category = response.css('.card-category::text').get().replace('category: ','')
           description = response.css('.card-text::text').get()
           
get() digunakan agar diambil datanya
kalau tanpa get, yang diambil selectornya