import os
import re

import requests
import json
import time
import random
import csv
from bs4 import BeautifulSoup

#该文件可以用来爬取知乎某问题下的回答文字并保存
#该文件也可以用来爬取某些钓鱼问题下的明星之类的图片
#需要输入问题的id号和指定页数

class ZhiHu(object):

    #用来爬取知乎回答
    def __init__(self):
        self.url = 'https://www.zhihu.com/api/v4/questions/{}/answers?' \
                   'include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment' \
                   '%2Creward_info%2Cis_collapsed%2Cannotation_action' \
                   '%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky' \
                   '%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count' \
                   '%2Ccan_comment%2Ccontent%2Ceditable_content' \
                   '%2Cattachment%2Cvoteup_count%2Creshipment_settings' \
                   '%2Ccomment_permission%2Ccreated_time%2Cupdated_time' \
                   '%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt' \
                   '%2Cis_labeled%2Cpaid_info%2Cpaid_info_content' \
                   '%2Crelationship.is_authorized%2Cis_author%2Cvoting' \
                   '%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B' \
                   '%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count' \
                   '%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A' \
                   '%5D.settings.table_of_content.enabled&limit=5&offset={}' \
                   '&platform=desktop&sort_by=default'

        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            'Accept-Encoding': 'gzip, deflate'
        }



    def get_comment(self,id,page):

        #id为问题的id
        #仅爬取文字内容
        pages = 0
        for bd in range(0,page):

            res = requests.get(url=self.url.format(id,pages),headers =self.headers ).content.decode('utf-8')

            data1 = json.loads(res)
            data = data1['data']

            pattern = re.compile(r'<[^>]+>',re.S)
            for item in data:
                author = item['author']['name']
                answer =item['content']
                answer = pattern.sub('',answer)
                with open('./zhihu.text', 'a', encoding='utf-8') as f:
                    f.write(author +'\n'+ answer + '\n')
                    f.write('\n')
                    f.write('\n')


            pages+=5
            time.sleep(random.randint(2,8))


    def get_pic(self,id,page):
        # id为问题的id
        pages = 0
        for c in range(0,page):
            res = requests.get(url=self.url.format(id, pages), headers=self.headers).content.decode('utf-8')
            data1 = json.loads(res)
            data = data1['data']

            for item in data:
                answer = item['content']
                res = re.compile(r'<noscript>(.*?)<noscript>')
                urls = res.findall(answer, re.S)

                res2 = re.compile(r'https://(.*?)\?')
                res3 = re.compile(r'\?')
                img_list = []


                for i in urls:

                    i = re.search(res2, i)
                    i = res3.sub('', i.group())
                    img_list.append(i)

                root = './images/'


                for i in range(0, len(img_list)):

                    path = root + str(time.time()) + '.jpg'
                    try:  # 创建或判断路径图片是否存在并下载
                        if not os.path.exists(root):
                            os.mkdir(root)
                        if not os.path.exists(path):
                            r = requests.get(img_list[i])
                            with open(path, 'wb') as f:
                                f.write(r.content)
                                f.close()
                                print("图片下载成功")
                        else:
                            print("文件已存在")
                    except:
                        print("爬取失败")

                    #随机休眠
                    time.sleep(random.randint(1,4))

            pages+=5



if __name__ =='__main__':
    a =ZhiHu()
    #a.get_comment(id = 20357247,page =10)
    a.get_pic(id = 40753170,page=20)