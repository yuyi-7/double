# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class SmSpider(scrapy.Spider):
    nema = '三明学院'
    allowed_domains = ['fjsmu.cn']
    start_urls = ['http://218.5.241.22:8036/JobInfo/showsublist.html?fid=11']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="newlist"]/ul')
        print(lists)
        title = lists.xpath('li/a/@title').extract()
        print(title)
        publishDate = lists.xpath('li/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == '20'+publishDate[i][1:9]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = '20'+publishDate[i][1:9]
                item['holdDate'] = holdDate
                item['url'] = 'http://218.5.241.22:8036'+url[i]
                yield item
            else:
                print('没有匹配')