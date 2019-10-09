import requests
import re
from bs4 import BeautifulSoup

if __name__ == "__main__":
    root_url = "https://koubei.baidu.com/s/med66.com?page=1&tab=comt"
    r = requests.get(root_url)
    print(r.encoding)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.prettify())
    data = {}
    data0 = {}
    comment0 = []
    #print(soup.find_all('pre'))
    comments = soup.find_all('pre')
    for comment in comments:
        data0['url'] = root_url
        comment0.append(comment.get_text())
        data0['comment'] = comment0
    #print(data0)

    page1 = 'https://koubei.baidu.com/s/med66.com?page=1&tab=comt'
    pattern1 = re.compile('page=\d+')
    pattern2 = re.compile('\d+')
    rx = re.search(pattern1, page1)
    rxx = re.search(pattern2, rx.group())
    print(rxx.group())