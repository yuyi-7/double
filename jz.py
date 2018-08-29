# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class JzSpider(scrapy.Spider):
    nema = '荆州职业技术学院'
    allowed_domains = ['jzit.net.cn']
    start_urls = ['http://jzit.91wllm.com/jobfair']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="infoBox mt10 b"]')
        print(lists)
        title = lists.xpath('ul[@class="infoList jobfairList"]/li[1]/a/@title').extract()
        print(title)
        publishDate = list(map(lambda x:x.strip(),lists.xpath('ul[@class="infoList jobfairList"]/li[5]/text()').extract()))
        holdDate = ""
        url = lists.xpath('ul[@class="infoList jobfairList"]/li[1]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://jzit.91wllm.com'+url[i]
                yield item
            else:
                print('没有匹配')