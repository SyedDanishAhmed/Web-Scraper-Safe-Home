# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:24:39 2019

@author: Tanvi
"""
from selenium import webdriver
import time
import pandas as pd
import os

def zillow (url,count):
    driver.get(url)
    p=".//div[@class='list-card-price']"
    t=".//div[@class='list-card-type']"
    a=".//h3"
    i=1
    price=[]
    type_house=[]  
    address=[]
    
    while(i<=count):
        p1 = driver.find_elements_by_xpath(p)
        for el in p1:
            price.append(el.text)
        t1 = driver.find_elements_by_xpath(t)
        for el in t1:
            type_house.append(el.text)  
        t1 = driver.find_elements_by_xpath(a)
        for el in t1:
            address.append(el.text)
        time.sleep(5)
        b="//*[@id='mobile-pagination-root']/div/ol/li[9]/a"
        btn =driver.find_element_by_xpath(b)
        btn.click()
        i+=1
    df= pd.DataFrame(list(zip(price, type_house, address)))
    df.columns=['Price', 'Type of House','Address']
    zillow_df.append(df,ignore_index=True)
    zillow_df.to_csv("zillow_scrape.csv")


columns=['Price', 'Type of House','Address of the Property']
zillow_df = pd.DataFrame(columns=columns)

driver = webdriver.Chrome()
url_pitt="https://www.zillow.com/homes/Pittsburgh-PA_rb/"
url_athen="https://www.zillow.com/homes/Athens-GA_rb/"
url_mad ="https://www.zillow.com/homes/Madison-WI_rb/"
url_buff="https://www.zillow.com/homes/Buffalo-NY_rb/"
count = 20
count_athen = 13
zillow(url_pitt,count) 
zillow(url_athen,count_athen) 
zillow(url_buff,count) 
zillow(url_mad,count) 

zillow_clean = pd.read_csv('zillow_scrape.csv')
zillow_clean[['Street','City','Combined']] = zillow_clean.Address.str.split(",",expand=True)
zillow_clean['Combined'] = zillow_clean['Combined'].str.strip()
zillow_clean['City'] = zillow_clean['City'].str.strip()
zillow_clean[['State','Zip']] = zillow_clean.Combined.str.split(" ",expand=True)
zillow_clean = zillow_clean.drop(['Combined','Address'],axis=1)

zillow_clean.to_csv("Zillow_Data_Final.csv",index=False)
os.remove("zillow_scrape.csv")


    
