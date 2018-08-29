# -*- coding: utf-8 -*-

import scrapy

from double.GetPresentTime import getPresentTime

from double.items import DoubleItem

from lxml import etree  #xpath 解析网页

from selenium import webdriver  #使用selenium来爬取js渲染的网页

class HnnySpider(scrapy.Spider):
    nema = '河南农业大学'
    allowed_domains = ['henau.edu.cn']
    start_urls = ['http://job.henau.edu.cn/plus/list.php?tid=5']

    def parse(self,response):
        item = DoubleItem()
        driver = webdriver.PhantomJS(service_log_path=r'../watchlog.log')  #初始化
        driver.get('http://job.henau.edu.cn/plus/list.php?tid=5')   #爬取网页
        html = etree.HTML(driver.page_source)  #转换格式
        #lists = response.xpath('//div[@class="newsBox"]')
        #print(lists)
        title = html.xpath('//div[@class="list_box"]/ul/li/a/@title')
        print(title)
        publishDate = html.xpath('//div[@class="list_box"]/ul/li/span/text()')
        holdDate = ""
        url = html.xpath('//div[@class="list_box"]/ul/li/a/@href')
        time = getPresentTime()
        #print('运行成功')
        for i in range(len(title)):
            if (title[i].find("招聘会") != -1 or title[i].find("双选会") != -1 or title[i].find("宣讲会") != -1  or title[i].find('供需见面会')!=-1) and time == publishDate[i][:10]:
                print(title[i])
                item['title'] = title[i]
                item['publishDate'] = publishDate[i][:10]
                item['holdDate'] = holdDate
                item['url'] = 'http://job.henau.edu.cn' + url[i]
                yield item
            else:
                print('没有匹配')