import scrapy
import time

class SpiderNcbi(scrapy.Spider):
    name = "influenza"

    def start_requests(self):
        urls = ['https://www.ncbi.nlm.nih.gov/genomes/FLU/Database/shipment.cgi']
        for url in urls:
            yield scrapy.FormRequest(
                url=url,
                formdata={
                    'SStatus': 'Released',
                    'SPartial': 'complete',
                    'VirusSpecies': '1',
                    'SSubtype': 'H3N2',
                    'SCountry': 'USA',
                    'SHost': 'Human',
                    'reportSamples': 'Set'
                }
            )

    def parse(self, response, **kwargs):
        # filename = f'influenza.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'saved file {filename}')
        for data in response.css('#Table7'):
            yield {
                # 'organism name': data.xpath('//tr[contains(@style, \'background-color: rgb(228, 236, 246)\')]/td[2]/text()').getall(),
                'protein': data.xpath('//tr[1]/td[3]/font/a/text()').getall()
            }
