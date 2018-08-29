# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem

from lxml import etree

from selenium import webdriver

class JxnySpider(scrapy.Spider):
    nema = '江西农业大学'
    allowed_domains = ['jxny.edu.cn']
    start_urls = ['http://jxndjy.jxau.edu.cn/module/jobfairs?type=']

    def parse(self,response):
        item = DoubleItem()
        driver = webdriver.PhantomJS(service_log_path=r'../watchlog.log')
        driver.get('http://jxndjy.jxau.edu.cn/module/jobfairs?type=')
        html = etree.HTML(driver.page_source)
        #lists = response.xpath('//div[@class="newsBox"]')
        #print(lists)
        title = html.xpath('//div[@class="text-eps w240"]/@title')
        print(title)
        publishDate = list(map(lambda x:x.strip() ,html.xpath('//table[@class="tb-pub-list"]/tbody/tr/td[2]/text()')))
        holdDate = ""
        #url = lists.xpath('ul/li[2]/a/@href').extract()
        time = getPresentTime()
        #print('运行成功')
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://jxndjy.jxau.edu.cn/module/jobfairs?type='
                yield item
            else:
                print('没有匹配')