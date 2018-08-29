# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class DzSpider(scrapy.Spider):
    nema = '德州学院'
    allowed_domains = ['dzu.edu.cn']
    start_urls = ['http://dzujy.dzu.edu.cn/a/zuijindongtai/']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="article-list floatL"]/ul')
        print(lists)
        title = lists.xpath('li/a/span/text()').extract()
        print(title)
        publishDate = lists.xpath('li/a/i/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://dzujy.dzu.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')