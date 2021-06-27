import os

import requests
import re
import random
import time
from bs4 import BeautifulSoup


#用来爬取微信文章照片
#有时候在微信文章上看到很多好看的图片想要下载
#主要用来收集一些摄影号的优秀照片
#本文件需要输入链接，然后会新建以该文章为标题的文件夹并下载文章中所有图片


class weixin(object):

    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            'Accept-Encoding': 'gzip, deflate'
        }


    def get_pic(self,url):
        #该函数用于 <img data-src=...>的情况
        #大部分的图片都在该标签下
        #会存在某些格式的图片例如.gif文件，但目标不是那些所以爬取
        r = requests.get(url=url,headers = self.headers)
        soup = BeautifulSoup(r.text,'html.parser')

        title = soup.find('h2',class_ = 'rich_media_title').text.strip()

        content1 = soup.find_all('img')

        root = './'+title+'/'


        for item in content1:
            try:
                url = item['data-src']
                path = root + str(time.time()) + '.jpg'
                try:
                    # 判断图片路径是否存在
                    if not os.path.exists(root):
                        os.mkdir(root)
                    if not os.path.exists(path):
                        c = requests.get(url)
                        with open(path, 'wb') as f:

                            f.write(c.content)
                            f.close()
                            print("图片下载成功")

                    else:
                        print('文件已存在')

                except:
                    print('爬取失败')

                #随机暂停1-4秒
                time.sleep(random.randint(1, 4))

            except:
                print('无图片可下载')



if __name__ =="__main__":
    a = weixin()
    a.get_pic(url = 'https://mp.weixin.qq.com/s/zBQB-qHgZOVPqrdNl40lJQ')