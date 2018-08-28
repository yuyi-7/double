# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HnlgSpider(scrapy.Spider):
    nema = '河南理工大学'
    allowed_domains = ['hpu.edu.cn']
    start_urls = ['http://www6.hpu.edu.cn/web5/jyzdwsylm/xwdt.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('body/div[2]/table[2]/tr/td[3]/table[2]')
        print(lists)
        title = lists.xpath('tr/td/a/text()').extract()
        print(title)
        publishDate = list(map(lambda x:x.strip(),lists.xpath('tr/td/text()').extract()))
        holdDate = ""
        url = lists.xpath('tr/td/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 and time == publishDate[i][1:]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][1:]
                item['holdDate'] = holdDate
                item['url'] = 'http://www6.hpu.edu.cn/web5'+url[i][2:]
                yield item
            else:
                print('没有匹配')