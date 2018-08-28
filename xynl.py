# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class XynlSpider(scrapy.Spider):
    nema = '信阳农林'
    allowed_domains = ['xyafc.edu.cn']
    start_urls = ['http://www.xyafu.edu.cn/jyxxw/tzgg/index.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="articleList articleList2"]/ul')
        print(lists)
        title = lists.xpath('li/a/@title').extract()
        print(title)
        publishDate = lists.xpath('li/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选周") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = r'http://www.xyafu.edu.cn/jyxxw/tzgg/'+url[i]
                yield item
            else:
                print('没有匹配')