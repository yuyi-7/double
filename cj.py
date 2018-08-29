# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class CjSpider(scrapy.Spider):
    nema = '长江大学'
    allowed_domains = ['yangtzeu.edu.cn']
    start_urls = ['http://yangtzeu.91wllm.com/jobfair']

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
                item['publishDate'] = publishDate[:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://yangtzeu.91wllm.com'+url[i]
                yield item
            else:
                print('没有匹配')