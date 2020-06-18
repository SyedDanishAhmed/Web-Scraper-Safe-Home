# -*- coding: utf-8 -*-
"""


Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed
          
This code merges all the crime data of the four cities together based on the common and important attributes.
"""


import pandas as pd

def merge_crime_clean_data():
    
    # Reading data for all cities
    buffalo_crime_clean = pd.read_csv('Buffalo_Crime_Clean_Zip.csv') 
    athens_crime_clean = pd.read_csv('Athens_Crime_Clean_Zip.csv') 
    madison_crime_clean = pd.read_csv('Madison_Crime_Clean_Zip.csv') 
    pittsburgh_crime_clean = pd.read_csv('Pittsburgh_Crime_Clean_Zip.csv') 
    
    buffalo_crime_clean = buffalo_crime_clean[buffalo_crime_clean.City == "BUFFALO"]
    athens_crime_clean = athens_crime_clean[athens_crime_clean.City == "ATHENS"]
    madison_crime_clean = madison_crime_clean[madison_crime_clean.City == "Madison"]
    pittsburgh_crime_clean = pittsburgh_crime_clean[pittsburgh_crime_clean.City == "Pittsburgh"]
        
    # Merging data for all cities
    crime_merged_all_cities = pd.concat([buffalo_crime_clean, athens_crime_clean, madison_crime_clean, pittsburgh_crime_clean])
    
    # Dropping na rows from the dataframe
    crime_merged_all_cities = crime_merged_all_cities.dropna()
    
    # Updating the casing of City column
    crime_merged_all_cities.City = crime_merged_all_cities.City.str.capitalize()
    
    #len(crime_merged_all_cities)
    # Writing merged data to csv
    crime_merged_all_cities.to_csv('crime_merged_all_cities.csv', index = False)
    
    return crime_merged_all_cities