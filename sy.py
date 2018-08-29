# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem

from lxml import etree  #xpath 解析网页

from selenium import webdriver  #使用selenium来爬取js渲染的网页

class SySpider(scrapy.Spider):
    nema = '邵阳学院'
    allowed_domains = ['hnsyu.net']
    start_urls = ['http://syxy.bibibi.net/module/jobfairs?type=']

    def parse(self,response):
        item = DoubleItem()
        driver = webdriver.PhantomJS(service_log_path=r'../watchlog.log')  #初始化
        driver.get('http://syxy.bibibi.net/module/jobfairs?type=')   #爬取网页
        html = etree.HTML(driver.page_source)  #转换格式
        #lists = response.xpath('//div[@class="newsBox"]')
        #print(lists)
        title = html.xpath('//ul[@id="data_html"]/li/div/div[2]/p[1]/a/@title')
        print(title)
        publishDate = html.xpath('//ul[@id="data_html"]/li/div/div[3]/div/p[1]/text()')
        holdDate = ""
        url = html.xpath('//ul[@id="data_html"]/li/div/div[2]/p[1]/a/@href')
        time = getPresentTime()
        #print('运行成功')
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://syxy.bibibi.net' + url[i]
                yield item
            else:
                print('没有匹配')