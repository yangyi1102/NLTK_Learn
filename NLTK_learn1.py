'''
Created on 2018年8月4日

@author: yangyi
'''
#coding=utf-8
import requests
import nltk
from bs4 import BeautifulSoup
import operator                  #operator模块是python中内置的操作符函数接口
from nltk.app.wordfreq_app import plot_word_freq_dist
class Learn(object):
    def HtmlGet(self):                    
        url='https://www.163.com/'
        html=requests.get(url)
        html.encoding='gb2312'
        tokens=[tok for tok in html.text.split()]
        print(tokens[0:1000])
    def PythonHtml(self):                     #解析网页
        url='https://python.org/'
        response=requests.get(url)
        #response.encoding='gb2312'
        html=BeautifulSoup(response.text,'lxml') 
        clean=html.get_text()
        tokens=[tok for tok in clean.split()]
        return tokens
    def freq_dis(self,tokens): #纯python统计频率
        freq_dis={}
        for tok in tokens:
            if tok in freq_dis:
                freq_dis[tok]+=1
            else:
                freq_dis[tok]=1
        sorted_ferq_dist=sorted(freq_dis.items(),key=operator.itemgetter(1),reverse=True)#对由字典排序 ，返回由tuple组成的List,不再是字典reverse = True  降序 或者 reverse = False 升序
        print('方法1')
        print(sorted_ferq_dist)
    def nltk_freq_dis(self,tokens):   #nltk统计频率
        Freq_dist_nltk=nltk.FreqDist(tokens)
        print('方法2')
        print(Freq_dist_nltk)
        for k,v in Freq_dist_nltk.items():
            print(str(k)+':'+str(v))
        return Freq_dist_nltk
    def Freq_dist_nltk_plot(self,Freq_dist_nltk):
        Freq_dist_nltk.plot(50,cumulative=False)
        
if __name__ == '__main__':
    t=Learn()
    #t.HtmlGet()
    res=t.PythonHtml()
    t.freq_dis(res)
    res1=t.nltk_freq_dis(res)
    t.Freq_dist_nltk_plot(res1)
    
    
    