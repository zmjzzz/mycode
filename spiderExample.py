from pandas import pandas
import scrapy

urllist = pandas.read_csv("E:/scrapy/all.csv")
for i in range(len(urllist)-1):
    urltxt=urllist['site'][i]
