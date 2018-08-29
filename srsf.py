# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem

from lxml import etree  #xpath 解析网页

from selenium import webdriver  #使用selenium来爬取js渲染的网页

class SrsfSpider(scrapy.Spider):
    nema = '上饶师范学院'
    allowed_domains = ['sru.jx.cn']
    start_urls = ['http://zsjy.sru.jx.cn/html/srsfzscjyyw/index.html']

    def parse(self,response):
        item = DoubleItem()
        driver = webdriver.PhantomJS(service_log_path=r'../watchlog.log')  #初始化
        driver.get('http://zsjy.sru.jx.cn/html/srsfzscjyyw/index.html')   #爬取网页
        html = etree.HTML(driver.page_source)  #转换格式
        #lists = response.xpath('//div[@class="newsBox"]')
        #print(lists)
        title = html.xpath('//span[@class="a-box"]/ul/li/a/text()')
        print(title)
        publishDate = html.xpath('//span[@class="a-box"]/ul/li/span/text()')
        holdDate = ""
        url = html.xpath('//span[@class="a-box"]/ul/li/a/@href')
        time = getPresentTime()
        #print('运行成功')
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i]
                item['holdDate'] = holdDate
                item['url'] = 'http://zsjy.sru.jx.cn' + url[i]
                yield item
            else:
                print('没有匹配')