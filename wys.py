# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class WysSpider(scrapy.Spider):
    nema = '武夷山职业学院'
    allowed_domains = ['wyszyxy.com']
    start_urls = ['http://www.wyszyxy.com/index.php?m=content&c=index&a=lists&catid=32']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//ul[@class="inf_lc"]')
        print(lists)
        title = lists.xpath('li/a[1]/@title').extract()
        print(title)
        publishDate = list(map(lambda x:x.strip(),lists.xpath('li/h4/span/text()').extract()))
        holdDate = ""
        url = lists.xpath('li/a[1]/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1)  and time[:7] == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = url[i]
                yield item
            else:
                print('没有匹配')