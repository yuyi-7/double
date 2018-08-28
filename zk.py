# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class ZkSpider(scrapy.Spider):
    nema = '周口职业技术学院'
    allowed_domains = ['zkvtc.edu.cn']
    start_urls = ['http://jiuye.zkvtc.edu.cn/14003/']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="gov-main"]/div/ul')
        print(lists)
        title = lists.xpath('li[@style=";"]/a/@title').extract()
        print(title)
        publishDate = lists.xpath('li[@style=";"]/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 and time == publishDate[i][1:11]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][1:11]
                item['holdDate'] = holdDate
                item['url'] = url[i]
                yield item
            else:
                print('没有匹配')