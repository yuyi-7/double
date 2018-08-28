# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class YcSpider(scrapy.Spider):
    nema = '宜春学院'
    allowed_domains = ['jxycu.edu.cn']
    start_urls = ['http://zsw.ycu.jx.cn/jyw/zphrl/list.htm']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@id="wp_news_w66"]/ul')
        print(lists)
        title = lists.xpath('li/div[1]/span[2]/a/@title').extract()
        print(title)
        publishDate = lists.xpath('li/div[2]/span/text()').extract()
        holdDate = ""
        url = lists.xpath('li/div[1]/span[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1 and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://zsw.ycu.jx.cn'+url[i]
                yield item
            else:
                print('没有匹配')