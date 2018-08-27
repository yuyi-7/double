# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class WxSpider(scrapy.Spider):
    nema = '皖西学院'
    allowed_domains = ['wxc.edu.cn']
    start_urls = ['http://job.wxc.edu.cn/2238/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="newslist"]/div/div/div/table')
        print(lists)
        title = lists.xpath('tr/td/table/tr/td[2]/a/text()').extract()
        print(title)
        publishDate = ""
        holdDate = ""
        url = lists.xpath('tr/td/table/tr/td[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1:  #and time[5:] == publishDate[i]
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = 'http://job.wxc.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')