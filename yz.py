# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class YzSpider(scrapy.Spider):
    nema = '永州职业技术学院'
    allowed_domains = ['hnyzzy.com']
    start_urls = ['http://www.hnyzzy.com/s/37/t/349/p/5/list.jspy']

    def parse(self, response):
        item = DoubleItem()
        #lists = response.xpath('//table[@class="table_style01"]')
        #print(lists)
        title = response.xpath('//div[@class="tdtext1"]/table/tr/td/a/font/text()').extract()
        print(title)
        publishDate = ''
        holdDate = ""
        url = response.xpath('//div[@class="tdtext1"]/table/tr/td/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1:# and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = 'http://www.hnyzzy.com'+url[i]
                yield item
            else:
                print('没有匹配')