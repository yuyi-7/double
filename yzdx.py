# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class YzdxSpider(scrapy.Spider):
    nema = '扬州大学农学院'
    allowed_domains = ['yzu.edu.cn']
    start_urls = ['http://yzu.91job.gov.cn/campus']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="infoBox mt10"]/ul')
        print(lists)
        title = lists.xpath('//ul[@class="infoList"]/li[@class="span7"]/a/text()').extract()[:20]
        print(title)
        publishDate = lists.xpath('//ul[@class="infoList"]/li[@class="span4"]/text()').extract()[:20]
        holdDate = ""
        url = lists.xpath('//ul[@class="infoList"]/li[@class="span7"]/a/@href').extract()[:20]
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1 ) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://yzu.91job.gov.cn'+url[i]
                yield item
            else:
                print('没有匹配')