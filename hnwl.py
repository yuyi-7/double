# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem

from lxml import etree  #xpath 解析网页

from selenium import webdriver  #使用selenium来爬取js渲染的网页

class HnwlSpider(scrapy.Spider):
    nema = '湖南文理学院'
    allowed_domains = ['huas.cn']
    start_urls = ['http://jy.huaszj.cn/module/jobfairs']

    def parse(self,response):
        item = DoubleItem()
        driver = webdriver.PhantomJS(service_log_path=r'../watchlog.log')  #初始化
        driver.get('http://jy.huaszj.cn/module/jobfairs')   #爬取网页
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
                item['url'] = 'http://jy.huaszj.cn' + url[i]
                yield item
            else:
                print('没有匹配')