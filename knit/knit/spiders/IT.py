import scrapy


class ScrapyKnit(scrapy.Spider):

    name = "it"
    base_url = 'http://knit.ac.in/coe/ODD_2016/btreg16xcdaz.asp?rollno='
    start_urls = [base_url+str(i) for i in range(15601, 15655)]

    def parse(self, response):
        elem = response.css('table')[5]
        yield{
            'marks': elem.css('td::text')[1].extract()
        }
