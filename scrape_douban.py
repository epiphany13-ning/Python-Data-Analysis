import requests
from bs4 import BeautifulSoup
# 使用一个更标准的 User-Agent 字符串
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
for start_num in range(0,250,25):#链接里面也是根据计算机索引，所以正好对应起来了
    #Chrome/91.0.4472.124 这个比较正规
    #Chrome/127.0.0.0 应该是插件的问题
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")#解析html内容
    #分析提取信息特点
    #findAll函数第一个参数：标签名 第二个参数可选
    #all_titles 是一个可迭代对象
    all_titles = soup.findAll("span",attrs = {"class":"title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
