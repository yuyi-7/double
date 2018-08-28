# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class NcSpider(scrapy.Spider):
    nema = '南昌大学'
    allowed_domains = ['ncu.edu.cn']
    start_urls = ['http://zjc.ncu.edu.cn/jy/index.php?c=channel&a=type&tid=68&page=1']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="am-u-md-9"]/ul[1]')
        print(lists)
        title = lists.xpath('li/a/text()').extract()
        print(title)
        publishDate = ''
        holdDate = ""
        url = lists.xpath('li/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 :#and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = 'http://zjc.ncu.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')