# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class JxnygcSpider(scrapy.Spider):
    nema = '江西农业工程学院'
    allowed_domains = ['jxaevc.com']
    start_urls = ['http://www.jxaevc.com/news/Index.asp']

    def parse(self, response):
        item = DoubleItem()
        #lists = response.xpath('//a[@class="listA" and @target="_self"]/@title').extract()
        #print(lists)
        title = response.xpath('//a[@class="listA" and @target="_self"]/@title').extract()
        print(title)
        publishDate = ''
        holdDate = ""
        url = response.xpath('//a[@class="listA" and @target="_self"]/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 :#and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = 'http://www.jxaevc.com'+url[i]
                yield item
            else:
                print('没有匹配')