# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class AqSpider(scrapy.Spider):
    nema = '安庆职业技术学院'
    allowed_domains = ['aqvtc.cn']
    start_urls = ['http://www.aqvtc.edu.cn/jiuye/206/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="wp_news_w71"]/table')
        print(lists)
        title = lists.xpath('tr/td[2]/a[2]/text()').extract()
        print(title)
        publishDate = lists.xpath('tr/td[4]/text()').extract()
        holdDate = ""
        url = lists.xpath('tr/td[2]/a[2]/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1)  and time[5:] == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www.aqvtc.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')