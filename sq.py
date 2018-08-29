# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class SqSpider(scrapy.Spider):
    nema = '商丘职业技术学院'
    allowed_domains = ['sqzy.edu.cn']
    start_urls = ['http://job.sqzy.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//table[@class="winstyle2456"]')
        print(lists)
        title = lists.xpath('tr/td[1]/a/@title').extract()
        print(title)
        publishDate = lists.xpath('tr/td[2]/text()').extract()
        holdDate = ""
        url = lists.xpath('tr/td[1]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://job.sqzy.edu.cn'+url[i]
                yield item
            else:
                print('没有匹配')