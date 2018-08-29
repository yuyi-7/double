# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HbkjsfSpider(scrapy.Spider):
    nema = '河北科技师范学院'
    allowed_domains = ['hevttc.edu.cn']
    start_urls = ['http://jiuye.hevttc.edu.cn/html/yuanxiaojianjie/nitoce/']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="col_r"]/div/ul')
        print(lists)
        title = lists.xpath('li/a/text()').extract()
        print(title)
        publishDate = lists.xpath('li/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选") != -1 or title[i].find("宣讲会") != -1)  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = url[i]
                yield item
            else:
                print('没有匹配')