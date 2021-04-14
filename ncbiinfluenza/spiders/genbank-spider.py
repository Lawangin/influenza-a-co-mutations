import json
import scrapy

# f = open('./../../genids.json')
# data = json.load(f)[0]
# for i in data['protein']:
#     print(i)

class SpiderNcbi(scrapy.Spider):
    name = "genbank"

    def start_requests(self):
        urls = ['https://www.ncbi.nlm.nih.gov/nucleotide/CY017131']
        for url in urls:
            yield scrapy.Request(
                url=url
            )

    def parse(self, response, **kwargs):
        # filename = f'genbank.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'saved file {filename}')
        yield {
            'aa': response.css('#feature_CY017131\.1_CDS_0 > a::text').getall()
        }