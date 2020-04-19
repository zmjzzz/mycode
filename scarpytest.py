import requests as req

import pandas as pd

import time

import re

url="http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=1&siteid=1&q=%E8%B5%B0%E7%A7%81&btnsearch="

Index=1

SleepNum = 3

dates=[]

titles=[]

nums=[]

while Index<123:
    my_essay - headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.95 Safari/537.36 Core/1.50.1280.400', }
    data = {'Param': '法院名称:****',

            'Index': Index, 'Page': '20', 'Order': '裁判日期', 'Direction': 'asc'}

    r=req.post(url, essay-headers=my_essay-headers, data = data)

    pattern1 = re.compile('"裁判日期":"(.*?)"', re.S)

    date = re.findall(pattern1, raw)

    pattern2 = re.compile('"案号":"(.*?)"', re.S)

    num = re.findall(pattern2, raw)

    pattern3 = re.compile('"案件名称":"(.*?)"', re.S)

    title = re.findall(pattern3, raw)

    # 把筛选出的数据添加到开始的三个空列表里

    dates += date

    titles += title

    nums += num

    # 这一行是让程序休息，做事留点余地比较好。通过抓取的网页框架可知，文书网是有验证码功能的，如果你抓的太狠中招莫怪。

    time.sleep(SleepNum)

    Index += 1

# 用pandas模块将筛选出的内容转成dataframe格式，并保存到Excel。

df = pd.DataFrame({'时间': dates, '案号': nums, '案件名称': titles})