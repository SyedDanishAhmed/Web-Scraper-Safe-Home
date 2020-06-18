# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:34:16 2019

@author: Tanvi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:24:39 2019

@author: Tanvi
"""
from selenium import webdriver
import time
import pandas as pd
import os

def zillow_rent (url,count):
    driver.get(url)
    p=".//div[@class='list-card-heading']"
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
    data_zillow= pd.DataFrame(columns=["Type Of House", "Address", "Price"])
    data_zillow['Type Of House'] = type_house
    data_zillow['Address'] = address
    data_zillow['Combined'] = price
    data_zillow.to_csv("Zillow.csv",index=False)


driver = webdriver.Chrome()
url_pitt="https://www.zillow.com/homes/Pittsburgh-PA_rb/"
url_athen="https://www.zillow.com/homes/Athens-GA_rb/"
url_mad ="https://www.zillow.com/homes/Madison-WI_rb/"
url_buff="https://www.zillow.com/homes/Buffalo-NY_rb/"
count_pitt = 20
count_athen = 7
count_buff = 13
count_madi = 14
zillow_rent(url_pitt,count_pitt) 
zillow_rent(url_athen,count_athen) 
zillow_rent(url_buff,count_buff) 
zillow_rent(url_mad,count_madi) 


zillow_clean=pd.read_csv('Zillow.csv')
zillow_clean['Combined'] = zillow_clean['Combined'].str.replace("/mo", " ")
data = zillow_clean
data= data.Combined.str.split(" ",expand=True)
zillow_clean['Price'] = data[0]
zillow_clean['Number of rooms'] = data[1]
zillow_clean['Price'] = zillow_clean['Price'].str.replace("$", "")
zillow_clean['Price'] = zillow_clean['Price'].str.replace(",", "")
zillow_clean['Price'] = zillow_clean['Price'].str.replace("+", "")
zillow_clean = zillow_clean[~zillow_clean['Number of rooms'].str.contains('Studio')]

data = zillow_clean.Address.str.split(",",expand=True)
zillow_clean['Street'] = data[0]
zillow_clean['City'] = data[1]
zillow_clean['StateZip'] = data[2]

zillow_clean['City'] = zillow_clean['City'].str.strip()
zillow_clean['Street'] = zillow_clean['Street'].str.strip()
zillow_clean['StateZip'] = zillow_clean['StateZip'].str.strip()
data = zillow_clean.StateZip.str.split(" ",expand=True)
zillow_clean['State'] = data[0]
zillow_clean['Zip'] = data[1]

zillow_clean = zillow_clean.drop(['StateZip','Address','Combined'],axis=1)
zillow_clean = zillow_clean.dropna()
zillow_clean = zillow_clean[~zillow_clean['Zip'].str.contains('sqft')]
zillow_clean = zillow_clean[~zillow_clean['Zip'].str.contains('Lafayette')]
zillow_clean['Zip'] = zillow_clean['Zip'].astype(int)
zillow_clean['Price'] = zillow_clean['Price'].astype(int)
zillow_clean.to_csv("Zillow_Data_Rent_Final.csv",index=False)
os.remove('Zillow.csv')

    
