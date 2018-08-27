# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class JhSpider(scrapy.Spider):
    nema = '金华职业技术学院'
    allowed_domains = ['jhc.cn']
    start_urls = ['http://news.jhc.cn/2262/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="wp_news_w6"]/ul')
        print(lists)
        title = lists.xpath('li/div/span/a/text()').extract()
        print(title)
        publishDate = lists.xpath('li/div[2]/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/div/span/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://news.jhc.cn'+ url[i]
                yield item
            else:
                print('没有匹配')