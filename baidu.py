from http import cookiejar
import random
import re
import time
import urllib.request
import urllib.parse
import urllib.error

import requests
from bs4 import BeautifulSoup


class spider:
    # 目标网站域名
    shh = 'www.baidu.com'
    site = 'http://' + shh
    # 需要点击的网站域名
    site_url = 'http://www.xxx.com'
    # 关键词
    keywords = [
        '关键词'
    ]
    # 访问每个页面的沉睡时间s
    sleep_time = 2
    # 虚拟user_agent
    user_agent = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

    # 百度统计数据
    sht = 'baiduhome_pg'
    Hjs = "http://hm.baidu.com/h.js?"
    Hgif = "http://hm.baidu.com/hm.gif?"
    UserAgent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'  # IE9
    MyData = {'cc': '1', 'ck': '1', 'cl': '32-bit', 'ds': '1024x768', 'et': '0', 'ep': '0', 'fl': '11.0', 'ja': '1',
              'ln': 'zh-cn', 'lo': '0', 'nv': '1', 'st': '3', 'v': '1.2.51'}
    TargetPage = ''
    refererPage = ''
    BaiduID = ''

    def __init__(self, baidu_id, site_url, keywords):
        # 域名
        self.site_url = site_url or self.site_url
        # 初始url
        self.start_url = self.site + '/s?wd={keyword}&ie=utf-8'
        # 百度id
        self.BaiduID = baidu_id
        self.MyData['si'] = self.BaiduID
        self.TargetPage = self.site_url
        self.keywords = keywords

    def run(self):
        start_time = time.time()
        # 循环关键词搜索
        for keyword in self.keywords:
            # 替换关键词到初始url
            url = self.start_url.replace('{keyword}', keyword)
            # 获取baidu爬到的目标网站点击链接
            final_url = self.getTargetUrl(url, keyword)
            if final_url is not False:
                # 将关键词添加到点击链接，对应百度搜索词
                self.refererPage = final_url + '&wd=' + keyword
                self.MyData['su'] = self.refererPage
                # 执行百度统计
                self.baidu(5)
                execute_time = time.time() - start_time
                print('执行时间：' + str(execute_time))

    def getTargetUrl(self, url, keyword):
        # 访问每个页面沉睡间隔
        time.sleep(self.sleep_time)
        f = requests.get(url, headers={'User-Agent': random.choice(self.user_agent)})
        soup = BeautifulSoup(f.content, 'lxml', from_encoding='utf-8')
        # 找到关键词所在的链接
        link = soup.find('a', text=re.compile(keyword))
        if link is None:
            # 找到下一页链接
            next = soup.find(name='a', attrs={'class': 'n'}, text='下一页>')
            if next is not None:
                next_url = self.site + next['href']
                return self.getTargetUrl(next_url, keyword)
            else:
                return False
        return link['href']

    def baidu(self, timeout=5):
        cj = cookiejar.CookieJar()

        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [("Referer", self.TargetPage), ("User-Agent", self.UserAgent)]
        try:
            opener.open(self.Hjs + self.BaiduID).info()
            self.MyData['rnd'] = int(random.random() * 2147483647)
            self.MyData['lt'] = int(time.time())
            tem_MyData = self.MyData
            tem_MyData['shh'] = self.shh
            tem_MyData['sht'] = self.sht
            tem_MyData['u'] = self.site_url
            tem_MyData['lv'] = '3'
            fullurl = self.Hgif + urllib.parse.urlencode(tem_MyData)
            opener.open(fullurl, timeout=timeout).info()
            self.MyData['rnd'] = int(random.random() * 2147483647)
            self.MyData['et'] = '3'
            self.MyData['ep'] = '2000,100'
            opener.open(self.Hgif + urllib.parse.urlencode(self.MyData), timeout=timeout).info()
            pass
        except urllib.error.HTTPError as ex:
            print(ex.code)
        except urllib.error.URLError as ex:
            print(ex.reason)


if __name__ == '__main__':
    spider('xxx', 'http://www.xxx.com', ['xxx']).run()
