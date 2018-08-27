# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class NdsnySpider(scrapy.Spider):
    nema = '宁德市农业学院'
    allowed_domains = ['ndgzy.com']
    start_urls = ['http://www.ndgzy.com/jyzd/list/407']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="artileListWraper"]')
        print(lists)
        title = lists.xpath('div/h3/a/text()').extract()
        print(title)
        publishDate = lists.xpath('div/div[@class="m-news-data"]/span[1]/text()').extract()
        holdDate = ""
        url = lists.xpath('div/h3/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://www.ndgzy.com'+url[i]
                yield item
            else:
                print('没有匹配')