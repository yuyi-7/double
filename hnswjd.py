# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HnswjdSpider(scrapy.Spider):
    nema = '湖南生物机电职业学院'
    allowed_domains = ['hnbemc.cn']
    start_urls = ['http://hnbemc.university-hr.cn/showmore.php?actiontype=1']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//table[@class="table_style01"]')
        print(lists)
        title = lists.xpath('tr[@class="trbg"]/td[2]/a/text()').extract()
        print(title)
        publishDate = lists.xpath('tr[@class="trbg"]/td[4]/text()').extract()
        holdDate = ""
        url = lists.xpath('tr[@class="trbg"]/td[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://hnbemc.university-hr.cn'+url[i]
                yield item
            else:
                print('没有匹配')