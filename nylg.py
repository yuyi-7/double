# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class NylgSpider(scrapy.Spider):
    nema = '南阳理工学院'
    allowed_domains = ['nyist.edu.cn']
    start_urls = ['http://nyist.jysd.com/news/index/tag/tzgg']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="newsBox"]')
        print(lists)
        title = lists.xpath('ul/li[2]/a/text()').extract()
        print(title)
        publishDate = lists.xpath('ul/li[1]/text()').extract()
        holdDate = ""
        url = lists.xpath('ul/li[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://nyist.jysd.com'+url[i]
                yield item
            else:
                print('没有匹配')