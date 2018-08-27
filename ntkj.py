# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class NtkjSpider(scrapy.Spider):
    nema = '南通科技职业学院'
    allowed_domains = ['ntst.edu.cn']
    start_urls = ['http://ntst.91job.gov.cn/news/index/tag/tzgg']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="newsBox"]')
        print(lists)
        title = lists.xpath('ul/li[2]/a/text()').extract()
        print(title)
        publishDate = lists.xpath('ul/li/text()').extract()
        holdDate = ""
        url = lists.xpath('ul/li[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://ntst.91job.gov.cn'+url[i]
                yield item
            else:
                print('没有匹配')