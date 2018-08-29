# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class AhnySpider(scrapy.Spider):
    nema = '安徽农业大学'
    allowed_domains = ['ahau.edu.cn']
    start_urls = ['http://job.ahau.edu.cn/tzgg/index.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//ul[@class="list-unstyled"]')
        print(lists)
        title = list(map(lambda x :x.strip(),lists.xpath('li/a/text()').extract()))
        print(title)
        publishDate = list(map(lambda x:x.strip(),lists.xpath('li/span/text()').extract()))
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1) and time[5:] == publishDate[i][1:6]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://job.ahau.edu.cn/tzgg/'+url[i]
                yield item
            else:
                print('没有匹配')