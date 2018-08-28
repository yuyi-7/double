# -*- coding: utf-8 -*-

import scrapy

import re

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class LczySpider(scrapy.Spider):
    nema = '聊城职业技术学院农牧科技系'
    allowed_domains = ['lctvu.sd.cn']
    start_urls = ['http://zsjyw.lcvtc.edu.cn/Article/Showclass.asp?classID=11']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//table[@id="__01"]/tr[2]/td[6]/table/tr[2]/td')
        print(lists)
        title = lists.xpath('a/text()').extract()
        print(title)
        times = lists.xpath('text()').extract()
        f = re.compile(r'\d{2}-\d{2}')
        b = list(map(lambda x:a.findall(x),times))
        publishDate = [x for x in b if len(x)!=0]
        holdDate = ""
        url = lists.xpath('a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find("供需见面会")!=-1 and time[5:] == publishDate[i][0]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://zsjyw.lcvtc.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')