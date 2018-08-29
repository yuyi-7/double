# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem


class SxnySpider(scrapy.Spider):
    nema = '山西农业大学'
    allowed_domains = ['sxau.edu.cn']
    start_urls = ['http://sxau.university-hr.com/showmore.php?actiontype=0']

    def parse(self, response):
        item = DoubleItem()
        lists = response.xpath('//div[@class="p2_m"]/div[2]/table')
        print(lists)
        title = lists.xpath('tr[@class="trbg"]/td[@align="left"]/a/text()').extract()
        print(title)
        publishDate = lists.xpath('tr[@class="trbg"]/td[4]/text()').extract()
        holdDate = ""
        url = lists.xpath('tr[@class="trbg"]/td[2]/a/@href').extract()
        time = getPresentTime()
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1)  and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                if url[i][:11] == 'showarticle':
                    item['url'] = 'http://sxau.university-hr.com/'+url[i]
                else:
                    item['url'] = url[i]
                yield item
            else:
                print('没有匹配')