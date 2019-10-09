import re
import urllib
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self, page_url, html_cont, page_number):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        #new_urls = self._get_new_urls(page_url, soup)
        new_urls = self._get_new_urls(page_url, page_number)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    #def _get_new_urls(self, page_url, soup):
    #更改后的网页抓取函数，利用现有网页直接拼凑翻页后的网页
    #https://koubei.baidu.com/s/med66.com?page=1&tab=comt => （下一页）
    #https://koubei.baidu.com/s/med66.com?page=2&tab=comt
    def _get_new_urls(self, page_url, page_number):
        new_urls = set()
        #links = soup.find_all('a', href=re.compile(r'//www'))
        link = 'https://koubei.baidu.com/s/med66.com?page=%d&tab=comt' % page_number
        new_urls.add(link)
        """
        for link in links:        
            #提取href属性
            new_url = link['href']
            #拼接成完整的网址
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            
            new_urls.add(link)
        """
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        comment0 = []
        user_name0 = []
        time0 = []
        score0 = []
        #当前爬取链接
        data['url'] = page_url
        #评论部分
        comments = soup.find_all('pre')
        if comments is None or len(comments) == 0:
            data['comment'] = ['无']
        else:
            for comment in comments:
                comment0.append(comment.get_text())
                data['comment'] = comment0
        #评论人
        user_names = soup.find_all(name='a', attrs={"hidefocus": 'hidefocus', "href": 'javascript:void(0)'})
        if user_names is None or len(user_names) == 0:
            data['user_name'] = ['无']
        else:
            for user_name in user_names:
                user_name0.append(user_name.get_text())
                data['user_name'] = user_name0

        #时间
        times = soup.find_all('span', class_='time')
        if times is None or len(times) == 0:
            data['user_name'] = ['无']
        else:
            for time in times:
                time0.append(time.get_text())
                data['time'] = time0

        #评分
        scores = soup.find_all('i', class_=re.compile(r'kb-i-small-star-\d'))
        if scores is None or len(scores) == 0:
            data['score'] = ['无']
        else:
            for score in scores:
                #评分在class属性里，需要提取
                real_score = str(score['class'])
                pattern = re.compile(r'\d')
                result = re.search(pattern, real_score)
                score0.append(result.group())
                data['score'] = score0

        return data


