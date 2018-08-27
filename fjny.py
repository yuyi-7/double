# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class FjnycSpider(scrapy.Spider):
    nema = '福建农业职业技术学院'
    allowed_domains = ['fjny.edu.cn']
    start_urls = ['http://job.fjny.edu.cn/news/news-list.php?id=2']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="listbox"]')
        print(lists)
        title = lists.xpath('div[@class="txt link_lan"]/h2/a/text()').extract()
        print(title)
        publishDate = lists.xpath('div[@class="txt link_lan"]/em[1]/text()').extract()
        holdDate = ""
        url = lists.xpath('div[@class="txt link_lan"]/h2/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = url[i]
                yield item
            else:
                print('没有匹配')