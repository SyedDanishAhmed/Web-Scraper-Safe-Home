#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Group 9 : Crime Patrol

Memebers: Tanvi Mittal
          Pooja Vasudevan
          Arkesh rath
          Syed Danish Ahmed
    
This code gives you the descriptive statistics of crime and real estate data for cities in US.

"""
# Imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
import numpy as np
import datetime as dt
from matplotlib import cm

def plotAverageRentPrices(data, NumberOfRooms):
    listPrices = []
    if data[data['Number of rooms'] == int(NumberOfRooms)].empty == False:
        data = data[data['Number of rooms'] == int(NumberOfRooms)]
    listings = pd.DataFrame(data)
    typeOfHouseAvg = pd.DataFrame(data['Type Of House'].unique())
    typeOfHouseAvg['AverageRent'] = 0
    for item in data['Type Of House'].unique():
        c = data[data['Type Of House'] == item]
        listPrices.append(c['Price'].mean())
    fig, ax = plt.subplots()
    typeOfHouseAvg['AveragePrice'] = listPrices
    ax.bar(typeOfHouseAvg[0], typeOfHouseAvg['AveragePrice'], label="Price")
    ax.legend()
    plt.xticks(rotation=90)
    plt.show()
    print(listings)
   

def plotAverageRentPricesWithZip(data,zipCode, NumberOfRooms='2'):
    listPrices = []
    if data[data['Number of rooms'] == int(NumberOfRooms)].empty == False:
        data = data[data['Number of rooms'] == int(NumberOfRooms)]
    data = data[data['Zip'] == int(zipCode)]
    listings = pd.DataFrame(data)
    if data.empty == False:
        typeOfHouseAvg = pd.DataFrame(data['Type Of House'].unique())
        typeOfHouseAvg['AverageRent'] = 0
        for item in data['Type Of House'].unique():
            c = data[data['Type Of House'] == item]
            listPrices.append(c['Price'].mean())
        fig, ax = plt.subplots()
        typeOfHouseAvg['AveragePrice'] = listPrices
        ax.bar(typeOfHouseAvg[0], typeOfHouseAvg['AveragePrice'], label="Price")
        ax.legend()
        plt.xticks(rotation=90)
        plt.show()
        print(listings)
    else:
        print('---------No Property Found----------')
    

def plotAveragePropertyPricesWithZip(data, zipCode, NumberOfRooms='2'):
    listPrices = []
    if data[data['Number of rooms'] == int(NumberOfRooms)].empty == False:
        data = data[data['Number of rooms'] == int(NumberOfRooms)]
    data = data[data['Zip'] == int(zipCode)]
    listings = pd.DataFrame(data)
    if data.empty == False:
        typeOfHouseAvg = pd.DataFrame(data['Type Of House'].unique())
        typeOfHouseAvg['AveragePrice'] = 0
        for item in data['Type Of House'].unique():
            c = data[data['Type Of House'] == item]
            listPrices.append(c['Price'].mean())
        fig, ax = plt.subplots()
        typeOfHouseAvg['AveragePrice'] = listPrices
        ax.bar(typeOfHouseAvg[0], typeOfHouseAvg['AveragePrice'], label="Price")
        ax.legend()
        plt.xticks(rotation=90)
        plt.show()
        print(listings)
    else:
        print('---------No Property Found----------')


def plotAveragePropertyPrices(data):
    listPrices = []
    typeOfHouseAvg = pd.DataFrame(data['Type Of House'].unique())
    for item in data['Type Of House'].unique():
        c = data[data['Type Of House'] == item]
        listPrices.append(c['Price'].mean())
    typeOfHouseAvg['Average Price'] = listPrices
    fig, ax = plt.subplots()
    ax.bar(typeOfHouseAvg[0], typeOfHouseAvg['Average Price'], label="Price")
    ax.legend()
    plt.xticks(rotation=90)
    plt.show()
 

def drawUpZipCode(data, zipCode):
    requiredData = data[data.Zip == int(zipCode)]
    sums = requiredData['Crime Category'].groupby(requiredData['Crime Category']).count()
    axis('equal');
    patches, texts = plt.pie(sums, startangle=90)
    plt.legend(patches,labels=sums.index, loc="best" ,  prop={'size': 6}, bbox_to_anchor=(1,0.5))
    plt.show()
   

def drawCityZipCode(data):
    sums = data['Crime Category'].groupby(data['Crime Category']).count()
    axis('equal');
    patches, texts = plt.pie(sums, startangle=90)
    plt.legend(patches, labels=sums.index ,  loc="best", prop={'size': 6}, bbox_to_anchor=(1,0.5))
    show()
   

def drawUpZipCodeBasedOnCrime(data, crime):
    requiredData = data[data['Crime Category'] == crime]
    sums = requiredData['Zip'].groupby(requiredData['Zip']).count()
    axis('equal');
    patches, texts = plt.pie(sums, startangle=90)
    plt.legend(patches, labels=sums.index , loc="best", prop={'size': 6}, bbox_to_anchor=(1,0.5))
    show()
    

def giveStats(data, zipCode, bedrooms, cityName):
    data = data[data['Number of rooms'] == int(bedrooms)]
    data = data[data['City'] == cityName]
    maxRent = np.max(data['Price'])
    minRent = np.min(data['Price'])
    averageRent = np.mean(data['Price'])
    dic = {'Zip Code':[int(zipCode)], 'Minimum Rent':[minRent], 'Maximum Rent':[maxRent], 'Average Rent': [averageRent]}
    stats = pd.DataFrame(dic)
    print(stats)
   

def giveStatsPerCity(data, bedrooms=2):
    data = data[data['Number of rooms'] == bedrooms]
    maxRent = data.groupby('Zip')['Price'].max()
    minRent = data.groupby('Zip')['Price'].min()
    averageRent = data.groupby('Zip')['Price'].mean()
    dic = {'Minimum Rent':minRent, 'Maximum Rent':maxRent, 'Average Rent': averageRent}
    stats = pd.DataFrame(dic)
    print(stats)
   

def checkScore(data, rent_data, zipCode, cityName, bedrooms):
    buffalo_area =  52.51
    pittsburgh_area =  58.34
    madison_area = 100.9
    athens_area = 118.2
    total_area = buffalo_area + pittsburgh_area + madison_area + athens_area
    cityData = rent_data[rent_data['City'] == cityName]
    cityData = cityData[cityData['Number of rooms'] == int(bedrooms)]
    data = data[data['Zip'] == int(zipCode)]
    frequency = data.groupby('Zip')['Severity Index'].sum()
    cityArea = 0
    if cityName == 'Pittsburgh':
        cityArea = pittsburgh_area
    elif cityName == 'Buffalo':
        cityArea = buffalo_area
    elif cityName == 'Madison':
        cityArea = madison_area
    else:
        cityArea = athens_area
    finalScore = (float(frequency) * float(cityArea))/float(total_area) 
    cityAveragePrice = cityData['Price'].mean()
    print('The average price of a ' + str(bedrooms) +' bedroom apartment is $' + str(cityAveragePrice))
    print('The safety score of the place is : ' + str(finalScore))
    

def findHouseToRent(data, rent_data,zipCode, bedrooms, cityName):
    plotAverageRentPricesWithZip(rent_data, zipCode, bedrooms)   
    drawUpZipCode(data, zipCode)
    giveStats(rent_data, zipCode, bedrooms)
    checkScore(data, rent_data, zipCode, cityName, bedrooms)


def findHouseToBuy(data, sale_data, zipCode, bedrooms, cityName):
    plotAveragePropertyPricesWithZip(sale_data, zipCode, bedrooms)   
    drawUpZipCode(data, zipCode)
    giveStats(sale_data, zipCode, bedrooms, cityName)
    checkScore(data, sale_data, zipCode, cityName, bedrooms)
   
   
def checkCity(data, rent_data, sale_data):
    drawCityZipCode(data)
    plotAveragePropertyPrices(rent_data)
    giveStatsPerCity(rent_data)


def price_data(zillow_df,zillow_rent_df):
    for i in range(0,len(zillow_df['Type Of House'])):
        if zillow_df['Type Of House'][i] == 'Foreclosed':
            zillow_df['Type Of House'][i]='Foreclosure'
        if zillow_df['Type Of House'][i] == 'Home for sale':
            zillow_df['Type Of House'][i]='House for Sale'
        if zillow_df['Type Of House'][i] == 'House for sale':
            zillow_df['Type Of House'][i]='House for Sale'
        if zillow_df['Type Of House'][i] == 'Pre-foreclosure / Auction':
            zillow_df['Type Of House'][i]='Pre-foreclosure'
    for i in range(0,len(zillow_rent_df['State'])):
        if zillow_rent_df['State'][i] == 'PA':
            zillow_rent_df['State'][i]='Pittsburgh'
        if zillow_rent_df['State'][i] == 'WI':
            zillow_rent_df['State'][i]='Madison'
        if zillow_rent_df['State'][i] == 'NY':
            zillow_rent_df['State'][i]='Buffalo'
        if zillow_rent_df['State'][i] == 'GA':
            zillow_rent_df['State'][i]='Athens'
    zillow_pricef = zillow_df.groupby(['Type Of House','State'])[['Price']].mean()
    zillow_rentPrice = zillow_rent_df.groupby(['Type Of House','State'])[['Price']].mean()
    fig, axs = plt.subplots(4, 1, figsize=(20,30), constrained_layout=True)
    zillow_rentPrice.unstack().plot.bar(rot=270,ax=axs[0])
    axs[0].set_title('Property Rentals by City', fontsize=20)
    axs[0].set_xlabel('Type Of House', fontsize=15)
    axs[0].set_ylabel('Price', fontsize=15)
    #fig.suptitle('This is a somewhat long figure title', fontsize=16)
    zillow_pricef.unstack().plot.bar(rot=270,ax=axs[1])
    axs[1].set_xlabel('Type Of House', fontsize=15)
    axs[1].set_title('Property Sales by City', fontsize=20)
    axs[1].set_ylabel('Price',fontsize=15)
    zillow_price = zillow_df.groupby('State')[['Price']].mean()
    #df = pd.DataFrame(zillow_price['Price'], index=index)
    zillow_price.plot.bar(rot=0, ax =axs[2])
    axs[2].set_xlabel('City', fontsize=15)
    axs[2].set_title('Average Sales Price for City', fontsize=20)
    axs[2].set_ylabel('Price',fontsize=15)  
    zillow_rent_price = zillow_rent_df.groupby('State')[['Price']].mean()
    #df = pd.DataFrame(zillow_price['Price'], index=index)
    zillow_rent_price.plot.bar(rot=0, ax =axs[3])
    axs[3].set_xlabel('City', fontsize=15)
    axs[3].set_title('Average Rent Price for City', fontsize=20)
    axs[3].set_ylabel('Price',fontsize=15)
    plt.show()


def crimes_per_month(merge_df):
    merge_df['Incident Date and Time']= pd.to_datetime(merge_df['Incident Date and Time'])
    merge_df['year'] = merge_df['Incident Date and Time'].dt.year
    merge_df['month'] = merge_df['Incident Date and Time'].dt.month
    merge_df_type = merge_df.groupby(['month','City'])[['Incident Type']].count()
    fig, ax = plt.subplots(figsize=(15,7))
    merge_df_type.unstack().plot(rot=0,kind='bar', stacked=True,ax=ax)
    ax.set_title('Crimes by Month', fontsize=20)
    ax.set_xlabel('Month', fontsize=15)
    ax.set_ylabel('Count of Crimes', fontsize=15)
    plt.show()

 
def crimes_month(merge_df,c,z):
    merge_df['Incident Date and Time']= pd.to_datetime(merge_df['Incident Date and Time'])
    merge_df['year'] = merge_df['Incident Date and Time'].dt.year
    merge_df['month'] = merge_df['Incident Date and Time'].dt.month
    df_city=merge_df[merge_df['City']==c]
    df_city=df_city[df_city.Zip==int(z)]
    df_crimes = df_city.groupby(['month'])[['Incident Type']].count()
    fig, ax = plt.subplots(figsize=(15,7))
    df_crimes.plot(rot=0,kind='bar',ax=ax)
    ax.set_title('Crimes by Month', fontsize=20)
    ax.set_xlabel('Month', fontsize=15)
    ax.set_ylabel('Count of Crimes', fontsize=15)
    plt.show()

  
def sales_stats(zillow_df,c,z):
    zillow_df1 = zillow_df[(zillow_df.City==c) & (zillow_df.Zip==int(z))]
    zillow_stats = zillow_df1.describe().loc[['min','max','mean']]
    print("Summary Statistics")
    print(zillow_stats['Price'])
    df_sales = zillow_df1.groupby(['Type Of House'])[['Price']].mean()
    fig, ax = plt.subplots(figsize=(15,7))
    df_sales.plot(rot=0,kind='bar',ax=ax)
    ax.set_title('Average Property Sales', fontsize=20)
    ax.set_xlabel('Type Of House', fontsize=15)
    ax.set_ylabel('Average Sales', fontsize=15)
    plt.show()
    

def crimes_by_city(merge_df):
    merge_df_crime = merge_df.groupby(['Crime Category','City'])[['Crime Category']].count()
    fig, ax = plt.subplots(figsize=(15,7))
    merge_df_crime.unstack().plot(rot=270,kind='bar',ax=ax)
    ax.set_title('Crimes by City', fontsize=20)
    ax.set_xlabel('Month', fontsize=15)
    ax.set_ylabel('Count of Crimes', fontsize=15)
    plt.show()


def crime_data(merge_df,c,z):
    merge_df_city = merge_df[merge_df.City==c]
    merge_df_city = merge_df_city[merge_df.Zip==int(z)]
    merge_df_crime = merge_df_city.groupby(['Crime Category'])[['Crime Category']].count()
    fig, ax = plt.subplots(figsize=(15,7))
    merge_df_crime.plot(rot=270,kind='bar',ax=ax)
    ax.set_title('Number of Crimes by Category', fontsize=20)
    ax.set_xlabel('Category', fontsize=15)
    ax.set_ylabel('Count of Crimes', fontsize=15)
    plt.show()