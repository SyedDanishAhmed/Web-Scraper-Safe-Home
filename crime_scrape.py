# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:27:38 2019

@author: Tanvi
"""
"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed

This file scrapes the crime data for the four university towns in USA, 
namely, Pittsburgh, Athens, Buffalo and Madison.
The scraping is done using Selenium and BeautifulSoup

"""

# Library Imports
import time
from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.support.ui import Select
import requests 
from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By

# Module import
import ZipExtractor as zp
#import zillow as zil
#import rent_zillow as zil_r

def athens_scrape():
    driver = webdriver.Chrome('chromedriver.exe')
    url_athens = "https://moto.data.socrata.com/dataset/ACCPD/8tt2-niit"
    driver.get(url_athens)
    # Getting the headers
    header ="(.//table)[3]/thead/tr"
#    header = ".//table/thead/tr"
    col = driver.find_elements_by_xpath(header)
    for c in col:
        headers = c.text.split("\n")
    row = "(.//tbody)[3]//tr"
#    row = ".//tbody/tr"
    final=[]
    count = 1
    btn = ".//button[contains(text(),'Next')]"
    time.sleep(2)
    # Get the data row wise for each page
#    while(count<3):
    while(count<300):
            rows = driver.find_elements_by_xpath(row)
            for element in rows:
                temp = element.text.split("\n")
                final.append(temp)
            count += 1
            button = driver.find_element_by_xpath(btn)
            button.click()
            time.sleep(5)
            
    # List of values to a dataframe
    athen_crime = pd.DataFrame(final)
    if 'clearance_type' in headers:
        headers.remove('clearance_type')
    if 'address_2' in headers:
        headers.remove('address_2')
    if 'country' in headers:
        headers.remove('country')
    athen_crime.columns=headers
    tempfilename = 'temp_crime_athens.csv'
    
    # Saving raw data
    athen_crime.to_csv(tempfilename,index=False)
    
    # Clean and save the data
    clean_athens = pd.read_csv(tempfilename)
    clean_athens = clean_athens.drop(['incident_description', 'created_at', 'updated_at','location','hour_of_day','day_of_week','parent_incident_type'], axis=1)
    clean_athens = clean_athens[~clean_athens['incident_datetime'].astype(str).str.startswith('19')]
    # Dropping the na values
    clean_athens = clean_athens.dropna()
    # Converting the Zip to integer
    clean_athens.zip = clean_athens.zip.astype(int)
    clean_athens = clean_athens[clean_athens.zip != 32]
    clean_athens = clean_athens[clean_athens.zip != 33]
    clean_athens = clean_athens[clean_athens.zip != 34]
    clean_athens = clean_athens[clean_athens.city == "ATHENS"]
    clean_athens.rename(columns={'zip':'Zip'},inplace = True)
    # Writing data to a file
    file_athen = 'athens_crime.csv'
    clean_athens.to_csv(file_athen,index=False)
    #Remove temporary files
    os.remove(tempfilename)
    driver.quit()
    return clean_athens



def buffalo_scrape():
    driver = webdriver.Chrome('chromedriver.exe')
    url_buffalo = "https://data.buffalony.gov/Public-Safety/Crime-Incidents/d6g9-xbgu/data"
    driver.get(url_buffalo)
    # Introducing delay to avoid robot detection
    time.sleep(5)
    row =".//tbody/tr"
    final=[]
    s = ".//button[contains(text(),'Next')]"
    button = driver.find_element_by_xpath(s)
    # Scraping data for 34 pages
    i = 0
#    while(driver.find_element_by_xpath(s).is_displayed() and i < 2):
    while(driver.find_element_by_xpath(s).is_displayed() and i < 34):
            l = driver.find_elements_by_xpath(row)
            for element in l:
                temp = element.text.split("\n")
                final.append(temp)
            button = driver.find_element_by_xpath(s)
            button.click()
            time.sleep(5)
            i += 1
    # List to dataframe
    crime_buffalo = pd.DataFrame(final)
    # Store the raw data
    temp = 'Buffalo_Raw.csv'
    crime_buffalo.to_csv(temp, index = None, header = True)
    # Updated column headers
    crime_buffalo.columns = ["incident_id", "case_number", "incident_datetime", "incident_time_primary", "incident_description","address_1", "City", "state", "Latitude", "Longitude", "created_date", "updated_date", "location", "hour_of_day", "day_of_week", "parent_incident_type", 'Sixteen']
    # Filtering for required rows and columns
    buff_treated = crime_buffalo[crime_buffalo['Sixteen'].isnull()]
    clean_buffalo = buff_treated.iloc[:,0:16]
    
    #Writing data to a file
    file_buffalo = 'buffalo_crime.csv'
    clean_buffalo.to_csv(file_buffalo, index=False)
    #Remove temporary files
    os.remove(temp)
    driver.quit()
    return clean_buffalo


def madison_scrape():
    driver = webdriver.Chrome('chromedriver.exe')
    url_madison = "http://data-cityofmadison.opendata.arcgis.com/datasets/police-incident-reports/data"
    driver.get(url_madison)
    time.sleep(5)
    final=[]
    try:
        last = ".//a[contains(text(),'»')]"
    except:
        last = "//*[@id='ember62']/nav/ul/li[14]/a"
    try:
        previous = """//*[@id="ember62"]/nav/ul/li[2]/a"""
    except:
        previous = ".//a[contains(text(),'«')]"
    time.sleep(5)
    button1 = driver.find_element_by_xpath(last)
    button1.click()
    count=0
    table = driver.find_element_by_xpath("""//*[@id="ember62"]/div[4]/table""")
    final=[]
    time.sleep(5)
    # Get the data row wise for each page
    while(driver.find_element_by_xpath(previous).is_displayed()):
        time.sleep(5)
        listings = table.find_elements(By.TAG_NAME, "tr")
        index=0
        for item in listings:
            temp = []
            # Get the column data for each row
            time.sleep(5)
            tds = item.find_elements(By.TAG_NAME, "td")
            for item in tds:
                temp.append(item.text)
            if len(temp) != 0:
                final.append(temp)
            index += 1
        time.sleep(5)
        button = driver.find_element_by_xpath(previous)
        button.click()
        count+=1
#        if count==1:
        if count==200:
            break
        time.sleep(5)
    # Clean the raw data
    crime_madison = pd.DataFrame(final)
    crime_madison.columns = ["IncidentID", "IncidentType","CaseNumber","IncidentDate","Suspect","Arrested" ,"Address","Victim","Details","ReleasedBy","DateModified"]
    clean_madison = crime_madison.drop(["Suspect","Arrested", "Victim","Details","ReleasedBy","DateModified"], axis=1)
    # Get the zipcode based on address for city of madison
    madison_zip = zp.zipExtractor(clean_madison)
    # Writing data to a file
    file_madison = 'madison_crime.csv'
    madison_zip.to_csv(file_madison,index=False)
    driver.quit()
    return clean_madison


def pitts_scrape():
    driver = webdriver.Chrome('chromedriver.exe')
    url_pitts = "https://data.wprdc.org/dataset/arrest-data/resource/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f/view/99669a9f-557f-4c35-9978-c83f0b457cb9"
    driver.get(url_pitts)
    time.sleep(2)
    select = Select(driver.find_element_by_xpath(".//select[@name='dtprv_length']"))
    select.select_by_visible_text('100')
    
    time.sleep(2)
    arrestBtn = driver.find_element_by_xpath(".//th[@scope='col' and contains(text(),'ARRESTTIME')]")
    driver.execute_script("arguments[0].click();", arrestBtn)
    
    time.sleep(1)
    arrestBtn = driver.find_element_by_xpath(".//th[@scope='col' and contains(text(),'ARRESTTIME')]")
    driver.execute_script("arguments[0].click();", arrestBtn)
    final_list=[]
    for i in range(0,50):
#    for i in range(0,1):
        time.sleep(2)
        element_list = driver.find_elements_by_xpath(".//tbody/tr")
        for element in element_list:
            list_2=[]
            td_list=element.find_elements_by_tag_name("td")
            for i in td_list:
                list_2.append(i.text)
            final_list.append(list_2)
        if(i!=49):
            driver.find_element_by_xpath(".//a[contains(text(),'Next')]").click()
    # Getting the headers
    r = requests.get(url_pitts) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    thead_list = soup.findAll('thead')
    col_list= [i.text for i in thead_list[0].findAll("th")]
    crime_pitts = pd.DataFrame(final_list, columns=col_list)
    tempfile= 'temp_crime_pitts.csv'
    crime_pitts.to_csv(tempfile,index = None, header = True)
    clean_pitts= pd.read_csv(tempfile)
    
    #Cleaning the data
    #Separating zip, address and state
    data = clean_pitts['INCIDENTLOCATION'].str.split(",",expand=True)
    data1 = data[1].str.split(" ", expand=True)
    clean_pitts['State'] = data1[1]
    clean_pitts['Zip Code'] = data1[2]
    city_list=[]
    for i in range(0, len(data[0])):
        list_1 = data[0][i].split(" ")
        city_list.append(list_1[len(list_1)-1])
    clean_pitts['City'] = city_list
    address_list=[]
    for i in range(0, len(data[0])):
        list_1 = data[0][i].split(" ")
        str=""
        for j in list_1:
            if j.strip() != "Pittsburgh":
                str+=j+" "
        address_list.append(str)
    clean_pitts['Address']=address_list
    del clean_pitts['INCIDENTLOCATION']
    # Renaming columns
    clean_pitts.rename(columns={'X':'Longitude','Y':'Latitude','_id':'ID','AGE':'Age','GENDER':'Gender',
                                'RACE':'Race','ARRESTTIME':'Arrest Date Time','ARRESTLOCATION':'Arrest Location',
                                'OFFENSES':'Offenses','INCIDENTNEIGHBORHOOD':'Incident Neighborbood',
                                'INCIDENTZONE':'Incident Zone','INCIDENTTRACT':'Incident Tract',
                                'COUNCILDISTRICT':'Council District','PUBLIC_WORKS_DIVISION':'Public Works Division','Zip Code':'Zip'},
                                inplace=True)
    clean_pitts = clean_pitts[clean_pitts.City == "Pittsburgh"]
    clean_pitts = clean_pitts[clean_pitts.State == "PA"] 
    
    #Writing data to a file
    file_pitts = 'pittsburgh_crime.csv'
    clean_pitts.to_csv(file_pitts,index=False)
    
    # Remove temporary file
    os.remove(tempfile)
    driver.quit()
    return clean_pitts


def lat_long_zip():
    url_lat_long="https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data"
    r = requests.get(url_lat_long)
    bsyc = BeautifulSoup(r.content, "html5lib")
    l= bsyc.text.split("\n")
    final_map=[]
    for el in l:
        final_map.append(el.split(","))
    df_map= pd.DataFrame(final_map[1:], columns=final_map[0])
    df_map['LNG'] = df_map['LNG'].str.strip()
    df_map.columns=['Zip','Latitude','Longitude']
    
    # Writing data to file
    file_map = 'Lat_Long_Zip.csv'
    df_map.to_csv(file_map, index = False)
    return df_map
