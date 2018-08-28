# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class HnnySpider(scrapy.Spider):
    nema = '湖南农业大学'
    allowed_domains = ['hunan.edu.cn']
    start_urls = ['http://jy.hunau.edu.cn//special/']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="speial_list_cont_w1000"]')
        print(lists)
        title = lists.xpath('div/div[@class="txt"]/div[1]/a/text()').extract()
        print(title)
        publishDate = '有报名截至时间'
        holdDate = ""
        url = lists.xpath('div/div[@class="txt"]/div[1]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 :#and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate
                item['holdDate'] = holdDate
                item['url'] = url[i]
                yield item
            else:
                print('没有匹配')