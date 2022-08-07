## 使用scrapy框架创建爬虫
```shell
scrapy startproject etherscan  # 会在当前目录创建一个etherscan目录
cd etherscan
scrapy genspider erc20_spider etherscan.io # 创建爬取erc20 token list信息的爬虫
```