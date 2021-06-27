import requests
from bs4 import BeautifulSoup


#有阅读英文版Chinadaily的习惯
#打开浏览器，输入网址、选择条目太慢了
#该文件会爬取chinadaily/world/下的三篇头条保存为txt格式并在指定目录下
#该文件可以与Windows的自动任务结合起来实现自动化，例如我设置了早上十点运行该程序


class Chinadaily(object):

    def __init__(self):
        self.url= '  '
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            'Accept-Encoding': 'gzip, deflate'
        }

    # 下载具体链接下的内容并保存到文件中
    def details_get(self,url):

        url = url
        r = requests.get(url=url,headers =self.headers)

        soup = BeautifulSoup(r.text,'html.parser')

        title = soup.find('div',class_ = "lft_art").h1.text.strip()

        content1 = soup.find('div',id= "Content")

        all_content = content1.find_all('p')
        path = 'D:/temp/daily/'
        try:
            #删除目录中的文件
            filelist=os.listdir(path)

            for f in filelist:
                filepath = os.path.join(path,f)
                os.remove(filepath)

        except:
            pass

        with open( path+title+'.txt','a',encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write('\n')

            for content in all_content:
                f.write(content.string)
                f.write('\n')
                f.write('\n')

    # 爬取chinadaily的首页三篇文章的链接
    def get_data(self):

        index_url = 'https://www.chinadaily.com.cn/world/'

        r = requests.get(url=index_url,headers = self.headers)
        soup = BeautifulSoup(r.text,'html.parser')

        urls = soup.find_all('div',class_='tBox')
        for item in urls:
            url1 = item.find('a')
            url = 'https:'+url1['href']
            self.details_get(url=url)









if __name__ =='__main__':
    a = Chinadaily()
    a.get_data()