from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager
import re

class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def get_url_page(self, url):
        pattern1 = re.compile('page=\d+')
        pattern2 = re.compile('\d+')
        rx = re.search(pattern1, url)
        rxx = re.search(pattern2, rx.group())
        url_page = int(rxx.group())
        return url_page

    def crawl(self, root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        page_number = self.get_url_page(root_url)
        #判断url管理器是否有新url，同时判断抓取了多少个url
        while(self.manager.has_new_urls() and self.manager.old_url_size() < 163):
            try:
                new_url = self.manager.get_new_urls()
                print(new_url)
                html = self.downloader.download(new_url)
                page_number += 1
                print('page=%s' % page_number)
                new_urls, data = self.parser.parser(new_url, html, page_number)
                #print(new_urls)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
                break
        print(self.output.datas)
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://koubei.baidu.com/s/med66.com?page=1&tab=comt")
