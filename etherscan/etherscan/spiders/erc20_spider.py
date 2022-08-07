import scrapy

from etherscan.items import ERC20TokenItem

class Erc20SpiderSpider(scrapy.Spider):
    name = 'erc20_spider'
    allowed_domains = ['etherscan.io']
    start_urls = ['https://etherscan.io/tokens']

    def parse(self, response):
        table = response.xpath('//*[@id="tblResult"]/tbody')
        for tr in table:
            token = ERC20TokenItem()
            name = tr.xpath('./td[2]/div/div/h3/a').extract()[0]
            print(name)
