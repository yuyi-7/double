# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class SxsfSpider(scrapy.Spider):
    nema = '山西师范大学'
    allowed_domains = ['sxnu.edu.cn']
    start_urls = ['http://xsc.sxnu.edu.cn/jyzdzx/xwzx.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="list_right fr"]/table')
        print(lists)
        title = lists.xpath('tr[@height="20"]/td[2]/a/@title').extract()
        print(title)
        publishDate = lists.xpath('tr[@height="20"]/td[3]/span/text()').extract()
        holdDate = ""
        url = lists.xpath('tr[@height="20"]/td[2]/a/@href')
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1) and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:-1]
                item['holdDate'] = holdDate
                item['url'] = 'http://xsc.sxnu.edu.cn'+url[i][2:]
                yield item
            else:
                print('没有匹配')