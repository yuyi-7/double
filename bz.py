# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class BzSpider(scrapy.Spider):
    nema = '槟州职业学院'
    allowed_domains = ['edubzvc.com.cn']
    start_urls = ['http://jyw.bzpt.edu.cn/s/88/t/75/p/1/c/889/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="newslist"]/table')
        print(lists)
        title = lists.xpath('tr/td[2]/table/tr/td/a/font/text()').extract()
        print(title)
        publishDate = ''
        holdDate = ""
        url = lists.xpath('tr/td[2]/table/tr/td/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1 or title[i].find('供需见面会')!=-1:# and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = 'http://jyw.bzpt.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')