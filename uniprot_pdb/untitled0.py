# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 09:02:01 2021

@author: iluvatar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import multiprocessing
import pandas as pd
import numpy as np



def task(protein):
    
    driver = webdriver.Chrome()
    
    url_template = "http://www.rcsb.org/pdb/files/{}.pdb"
    
    protein = protein
    
    url = url_template.format(protein)
    
    response = urllib2.urlopen(url)
    
    pdb = response.read().decode('utf-8')
    
    response.close()
    
    m = re.search('UNP\ +(\w+)', pdb)
    
    code = m.group(1)
    
    url_1 = 'https://www.uniprot.org/uniprot/'
    
    url_2 = '#showFeaturesTable'
    
    # code = 'Q02MM2'
    
    code = 'P21802'
    
    url = url_1 + code + url_2
    
    driver.get(url)
    
    time.sleep(5)
    
    data = driver.page_source
    
    soup=BeautifulSoup(data)
    
    
    
    try:
        
        f = open(protein+ '_' + code +'_mut.txt','w',encoding="utf-8")
          
        mut_table = soup.find_all('table',{'id':"Mutagenesis_section"})[0].find_all('tr')[1::]
        
        for i in mut_table:
        
            ii = i.find_all('td')
            
            site_num = ii[1].text
            
            # mut_before = ii[2].text.split('.')[0].split(':')[0].split(' → ')[0]
            
            # mut_after = ii[2].text.split('.')[0].split(':')[0].split(' → ')[1]
            
            mut_des_ = ii[2].text.split('.')[0].split(':')[0]
            
            mut_des = ii[2].text.split('.')[0].split(':')[1][1::]
            
            pub = []
            
            for j in ii[2].find_all('div',{'property':"citation"}):
                
                pub.append(j.find_all('strong')[0].text)
            
            print(site_num)
            
            # print(mut_before)
            
            # print(mut_after)
            
            print(mut_des_)
            
            print(mut_des)
            
            print(pub)
            
            f.write(site_num)
            
            f.write('\t')
            
            f.write(mut_des_)
            
            f.write('\t')
            
            f.write(mut_des)
            
            f.write('\t')
            
            f.write(str(pub))
            
            f.write('\n')
        
        f.close()
            
            
    
    except:
        
        f.close()
        
        pass
    
    
        
    try:
        
        f = open(protein+ '_' + code+'_var.txt','w', encoding="utf-8")
        
        var_table = soup.find_all('table',{'id':"Natural_variant_section"})[0].find_all('tr')[1::]
        
        for i in var_table:
        
            ii = i.find_all('td')
            
            site_num = ii[1].text
            
            # var_before = ii[2].text.split('.')[0].split(':')[0].split(' → ')[0]
            
            # var_after = ii[2].text.split('.')[0].split(':')[0].split(' → ')[1]
            
            
            var_des = ii[2].text.split('.')[0]
            
            # var_des = ii[2].text.split('.')[0].split(':')[1][1::]
            
            pub = []
            
            for j in ii[2].find_all('div',{'property':"citation"}):
                
                try:
                    
                    pub.append(j.find_all('strong')[0].text)
                
                except:
                    
                    pub.append(j.text)
            
            print(site_num)
            
            # print(var_before)
            
            # print(var_after)
            
            # print(var_des_)
            
            print(var_des)
            
            print(pub)
            
            f.write(site_num)
            
            f.write('\t')
            
            f.write(mut_des_)
            
            f.write('\t')
            
            f.write(mut_des)
            
            f.write('\t')
            
            f.write(str(pub))
            
            f.write('\n')
        
        f.close()
            
    except:
        
        f.close()
        
        pass