import os
import re

import requests
import random
import time
from bs4 import BeautifulSoup


#wallhaven.cc上有太多好看的壁纸一张张下载太慢了
#该文件会下载指定页数下的所有壁纸
class PIC(object):


    def __init__(self):
        self.url = 'https://wallhaven.cc/latest?page={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }


    #获取随机条目下的壁纸
    def get_random_pic(self,page):
        url = 'https://wallhaven.cc/random?seed=ErCdOs&page={}'
        page = page
        self.get_onepage(url = url,page=page)

    #获取最新的壁纸
    def get_last_pic(self,page):
        url = 'https://wallhaven.cc/latest?page={}'
        page = page
        self.get_onepage(url = url,page=page)

    def get_onepage(self,url,page):
        #爬取一页下的所有壁纸

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        for pages in range(0,page):
            url = url.format(pages)

            #该网站响应速度并不是很快
            r = requests.get(url=url,headers=headers,timeout=3).text
            soup = BeautifulSoup(r,'html.parser')

            img_text = soup.find_all('a',class_="preview")

            for item in img_text:
                img1_url = item['href']

                r1 = requests.get(url = img1_url,headers=headers,timeout = 10).text
                soup1 = BeautifulSoup(r1,'html.parser')

                img_url = soup1.find('div',class_="scrollbox").img
                img_url=img_url['src']


                root = './wallhaven/'
                path = root + str(time.time()) + '.jpg'
                try:
                    # 创建或判断路径图片是否存在并下载
                    if not os.path.exists(root):
                        os.mkdir(root)
                    if not os.path.exists(path):
                        r = requests.get(img_url)
                        with open(path, 'wb') as f:
                            f.write(r.content)
                            f.close()
                            print("图片下载成功")
                    else:
                        print("文件已存在")
                except:
                    print("爬取失败")
                #随机休眠1-20秒
                time.sleep(random.randint(1,20))

if __name__=='__main__':
    a= PIC()
    a.get_last_pic(page=10)


    #c = [<a class="preview" href="https://wallhaven.cc/w/575y57" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/wq651p" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/v9opzm" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/q23rrq" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/v9z3d8" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/3z3g6d" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/28zjom" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/y8eqq7" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/3zwqld" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/v9opq8" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/6o5ldl" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/m91l31" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/721jp9" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/wq65q7" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/l3wy8q" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/28d18m" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/y8eqx7" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/dpk8pj" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/o31g55" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/z8qp8v" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/rdyqd1" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/q23r25" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/k71876" target="_blank"></a>, <a class="preview" href="https://wallhaven.cc/w/8okg5j" target="_blank"></a>]