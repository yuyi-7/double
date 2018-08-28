# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class NysfSpider(scrapy.Spider):
    nema = '南阳师范学院'
    allowed_domains = ['nynu.edu.cn']
    start_urls = ['http://www2.nynu.edu.cn/xzbm/jiuye/class.aspx?Newsclass=%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//table[@id="GridView1"]')
        print(lists)
        title = lists.xpath('tr/td/a/span/text()').extract()
        print(title)
        publishDate = lists.xpath('tr/td/span/text()').extract()
        holdDate = ""
        url = lists.xpath('tr/td/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 :#and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www2.nynu.edu.cn/xzbm/jiuye/'+url[i]
                yield item
            else:
                print('没有匹配')