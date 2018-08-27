# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class FjnlSpider(scrapy.Spider):
    nema = '福建农林大学'
    allowed_domains = ['fafu.edu.cn']
    start_urls = ['http://www.fafu.edu.cn/5276/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="wp_news_w3"]/table')
        print(lists)
        title = lists.xpath('tbody/tr/td[2]/table/tr/td/a/@title').extract()
        print(title)
        publishDate = lists.xpath('tbody/tr/td[2]/table/tr/td[2]/div/text()').extract()
        holdDate = ""
        url = lists.xpath('tbody/tr/td[2]/table/tr/td/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www.fafu.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')