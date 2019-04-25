# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:08:30 2019

@author: 30517
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
lista=[]

#
f = open('gene.txt','r',encoding='utf8')
for i in f:
    if i !='':
        print(i)
        driver = webdriver.Chrome()
        driver.get('http://omim.org/search/?index=entry&start=1&limit=10&sort=score+desc%2C+prefix_sort+desc&search='+i)
        
        time.sleep(10)
        data = driver.page_source
            
            
        soup=BeautifulSoup(data)
        d=soup.find_all('span',{'class':"mim-result-font"})[0].find_all('span',{'class':"mim-qtipHint"})[0].text.replace('\n*\n','').replace('.\n','')
        lista.append(d)
        print(d)
        driver.quit()
        time.sleep(5)
        