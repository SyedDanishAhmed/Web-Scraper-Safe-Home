# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:52:08 2019

@author: Tanvi
"""

"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed
          
This code gets the latitude and longitude based on the zipcode.
"""


import pandas as pd

def zip_map_pittsburgh():
    
    # Reading data for all cities
    df = pd.read_csv('crime_pittsburgh.csv') 
    # Filtering the data set for required columns
    df_updated = df[["ID", "Arrest Date Time", "Offenses", "Incident Neighborhood", "City", "State", "Zip Code", "Latitude", "Longitude"]]
    # Updating headers
    df_updated.columns = ["ID", "Incident Date and Time", "Incident Type", "Street", "City", "State", "Zip", "Latitude", "Longitude"]
    
    df_updated.to_csv('Pittsburgh_Crime_Clean_Zip.csv', index = None, header = True)
    return df_updated


def zip_map_buffalo():
    
    # Reading data for all cities
    df = pd.read_csv('crime_buffalo.csv') 
    # Filtering the data set for required columns
    df_updated = df[["incident_id", "incident_datetime", "incident_type", "address_1", "City", "state", "Latitude", "Longitude"]]
    
    df_updated['Lat'] = df_updated['Latitude'] 
    df_updated['Lon'] = df_updated['Longitude'] 
    
    # Rounding off the latitude and longitude to given decimal places for mapping to zip codes
    decimals = 1
    df_updated['Latitude'] = df_updated['Latitude'].apply(lambda x: round(x, decimals))
    df_updated['Longitude'] = df_updated['Longitude'].apply(lambda x: round(x, decimals))
    
    # Reading file for latitude, longitude and zip mapping
    zip_latlon_map = pd.read_csv("Lat_Long_Zip_Map.csv")
    
    # Rounding off the latitude and longitude to given decimal places for mapping to zip codes
    decimals = 1   
    zip_latlon_map['Latitude'] = zip_latlon_map['Latitude'].apply(lambda x: round(x, decimals))
    zip_latlon_map['Longitude'] = zip_latlon_map['Longitude'].apply(lambda x: round(x, decimals))
        
    # Merging to get zip codes
    zip_mapped = pd.merge(df_updated, zip_latlon_map, on= ['Latitude', 'Longitude'], how='inner')
    zip_mapped = zip_mapped.drop_duplicates(subset='incident_id', keep="first")
    len(zip_mapped)
    
    zip_mapped = zip_mapped[["incident_id", "incident_datetime", "incident_type", "address_1", "City", "state", "Zip", "Lat", "Lon"]]
    
    zip_mapped.columns = ["ID", "Incident Date and Time", "Incident Type", "Street", "City", "State", "Zip", "Latitude", "Longitude"]
    
    len(zip_mapped.Zip.unique())
    
    zip_mapped.to_csv('Buffalo_Crime_Clean_Zip.csv', index = None, header = True)
    return zip_mapped
    

def zip_map_madison():
    
    # Reading data for all cities
    df = pd.read_csv('crime_madison.csv') 
    
    df['City'] = 'Madison'
    df['State'] = 'WI'
    
    # Filtering the data set for required columns
    df_updated = df[["IncidentID", "IncidentDate", "IncidentType", "Address", "City", "State", "Zip"]]
    
    # Reading file for latitude, longitude and zip mapping
    zip_latlon_map = pd.read_csv("Lat_Long_Zip_Map.csv")
    
    # Merging to get zip codes
    zip_mapped = pd.merge(df_updated, zip_latlon_map, on= ['Zip'], how='inner')
    
    # Updating column names
    zip_mapped.columns = ["ID", "Incident Date and Time", "Incident Type", "Street", "City", "State", "Zip", "Latitude", "Longitude"]
    
    #len(zip_mapped.Zip.unique())
    
    zip_mapped.to_csv('Madison_Crime_Clean_Zip.csv', index = None, header = True)
    
    return zip_mapped
    
def zip_map_athens():
    
    # Reading data for all cities
    df = pd.read_csv('crime_athens.csv') 
    
    # Filtering the data set for required columns
    df_updated = df[["incident_id", "incident_datetime", "incident_type_primary", "address_1", "city", "state", "zip", "latitude", "longitude"]]
    
    # Standardizing the column names
    df_updated.columns = ["ID", "Incident Date and Time", "Incident Type", "Street", "City", "State", "Zip", "Latitude", "Longitude"]
    
        
    df_updated.to_csv('Athens_Crime_Clean_Zip.csv', index = None, header = True)
    return df_updated
