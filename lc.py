# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class LcSpider(scrapy.Spider):
    nema = '聊城大学'
    allowed_domains = ['lcu.edu.cn']
    start_urls = ['http://www.lcu.edu.cn/ztzx/ldyw/index.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="article cur02"]/ul')
        print(lists)
        title = list(map(lambda x:x.strip() , lists.xpath('li/a/text()').extract()))
        print(title)
        publishDate = lists.xpath('li/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www.lcu.edu.cn/ztzx/ldyw/'+url[i]
                yield item
            else:
                print('没有匹配')