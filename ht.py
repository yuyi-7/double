# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HtSpider(scrapy.Spider):
    nema = '河套学院'
    allowed_domains = ['hetaodaxue.com']
    start_urls = ['http://www.hetaodaxue.com/jyzdzx/index/gg.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="newsnr"]/div/ul')
        print(lists)
        title = lists.xpath('li/a/text()').extract()
        print(title)
        publishDate = lists.xpath('li/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www.hetaodaxue.com/jyzdzx'+url[i][5:]
                yield item
            else:
                print('没有匹配')