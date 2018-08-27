# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HbnySpider(scrapy.Spider):
    nema = '河北农业大学'
    allowed_domains = ['hebau.com']
    start_urls = ['http://jiuye.hebau.edu.cn/news2/js1.html']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath("//div[@class='info_list']")
        print(lists)
        title = lists.xpath('/ol/a/text()').extract()
        print(title)
        publishDate = lists.xpath('ol/span/text()').extract()
        holdDate = ""
        url = lists.xpath('ol/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("校园招聘") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://jiuye.hebau.edu.cn/news2/'+url[i]
                yield item
            else:
                print('没有匹配')