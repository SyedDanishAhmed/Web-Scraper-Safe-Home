# -*- coding: utf-8 -*-
"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed
          
This file is the main file that call all the functions which 
scrapes, clean, merge and analyze crime and property data.
The user is provided with a menu where they can select what 
kind of statistics they would want to view.
"""


# Library Imports 
import time
import pandas as pd
from os import path
        
# Modules Imports
import zip_map
import merge_crime_clean_data as merge
import map_crime_category as category
import crime_scrape as scrape
import analyzer as analyze
import severity_index as severe

def chooseCity():
    print(''' 
    Please select a city number:
    1)  Pittsburgh
    2)  Madison
    3)  Buffalo
    4)  Athens
    ''')
    city = input('    Your choice: ').strip()
    return city

def chooseZip(category_map,city):
    if city == '1':
        name = 'Pittsburgh'
    elif city == '2':
        name = 'Madison'
    elif city == '3':
        name = 'Buffalo'
    elif city == '4':
        name = 'Athens'
    print(''' 
    Please select a zip code from the following:
    ''')
    print(category_map[category_map['City'] == name].Zip.unique())
    zipCode = input('    Your choice: ').strip()
    return zipCode

def chooseBedRoom():
    print(''' 
    Please enter the number of bedrooms you want:
    ''')
    bed = input('    Your choice: ').strip()
    return bed

if __name__ == "__main__":
    answer = 0
    counter = 0
    while answer != '14':
        if counter == 0:
            counter = counter + 1
            print('''
            Welcome to Crime Patrol!
            We help you find the safest and most affordable places to stay at while you are attending college.
            ''')
            print('''
                  Please choose an option:
                1) Would you like to scrape the data
                2) Use pre-scraped data and proceed
                ''')  
            choice = input('    Your choice: ').strip()
            if choice == '1':
                # Function call to scrape the crime data and store in a dataframe for every city
#                clean_buffalo = scrape.buffalo_scrape()
#                time.sleep(2)
#                clean_athens = scrape.athens_scrape()
#                time.sleep(2)
#                clean_pitts = scrape.pitts_scrape()
#                time.sleep(2)
                clean_madison = scrape.madison_scrape()
                time.sleep(2)
                # Scrape the Zipcode mapping to Latitude Longitude for USA
                df_map = scrape.lat_long_zip()
            elif choice == '2':
                file_buffalo = 'crime_buffalo.csv'
                file_athen = 'crime_athens.csv'
                file_madison = 'crime_madison.csv'
                file_pitts = 'crime_pittsburgh.csv'
                file_map = 'Lat_Long_Zip_Map.csv'
                clean_buffalo = pd.read_csv(file_buffalo)
                clean_athens = pd.read_csv(file_athen)
                clean_madison = pd.read_csv(file_madison)
                clean_pitts = pd.read_csv(file_pitts)
                df_map = pd.read_csv(file_map)
            sale="Zillow_Data.csv"
            rent="Zillow_Data_Rent.csv"
            zillow_sale = pd.read_csv(sale)
            zillow_rent = pd.read_csv(rent)
            
            # Mergeing the crime data
            clean_pitts = zip_map.zip_map_pittsburgh()
            clean_athens = zip_map.zip_map_athens()
            clean_madison = zip_map.zip_map_madison()
            clean_buffalo = zip_map.zip_map_buffalo()
            merged_crime = merge.merge_crime_clean_data()
            if(path.exists("category_mapped_crime_merged.csv")):
                category_map = pd.read_csv('category_mapped_crime_merged.csv')
            else: 
                category_map = category.map_crime_category()
            if(path.exists("severity_category_mapped_crime.csv")):
                severity = pd.read_csv('severity_category_mapped_crime.csv')
            else: 
                severity = severe.severity_index()
        
        print('''
              
        Please select from the given menu:
    
        1)  Look up Crime Statistics for your chosen Zip Code
        2)  Look up Real Estate Pricings for your chosen Zip Code
        3)  Find a house/apartment to Rent
        4)  Find a house/apartment to Buy
        5)  Compare safe areas across Cities
        6)  Compare housing prices across Cities
        7)  Look up Crime Statistics for your chosen City 
        8)  Look up Real Estate Pricings for your chosen City
        9)  Look up Overall Crime Statistics for your chosen City and Zip Code
        10) Look up Property Sale Satistics for your chosen City and Zip Code
        11) Look up Property Rent Satistics for your chosen City and Zip Code
        12) Look up General Statistics on Crimes per category across Cities
        13) Look up number of crime per category for your chosen City and Zip Code
        14) Quit from this program
        ''')
        answer = input('    Your choice: ').strip()
        if answer == '1':
            city = chooseCity()
            zipCode = chooseZip(category_map,city)
            if city == '1':
                analyze.drawUpZipCode(category_map,zipCode)
            elif city == '2':
                analyze.drawUpZipCode(category_map,zipCode)
            elif city == '3':
                analyze.drawUpZipCode(category_map,zipCode)
            elif city == '4':
                analyze.drawUpZipCode(category_map,zipCode)
        
        elif answer == '2':
            city = chooseCity()
            zipCode = chooseZip(zillow_rent,city)
            if city == '1':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '2':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '3':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '4':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
                
        elif answer == '3':
            city = chooseCity()
            zipCode = chooseZip(category_map,city)
            bedroom = chooseBedRoom()
            if city == '1':
                analyze.findHouseToRent(severity,zillow_rent,zipCode,bedroom,'Pittsburgh')
            elif city == '2':
                analyze.findHouseToRent(severity,zillow_rent,zipCode,bedroom,'Madison')
            elif city == '3':
                analyze.findHouseToRent(severity,zillow_rent,zipCode,bedroom,'Buffalo')
            elif city == '4':
                analyze.findHouseToRent(severity,zillow_rent,zipCode,bedroom,'Athens')
                
        elif answer == '4':
            city = chooseCity()
            zipCode = chooseZip(category_map,city)
            zillow_sale['Number of rooms'] = 2
            if city == '1':
                analyze.findHouseToBuy(severity,zillow_sale,zipCode,bedroom,'Pittsburgh')
            elif city == '2':
                analyze.findHouseToBuy(severity,zillow_sale,zipCode,bedroom,'Madison')
            elif city == '3':
                analyze.findHouseToBuy(severity,zillow_sale,zipCode,bedroom,'Buffalo')
            elif city == '4':
                analyze.findHouseToBuy(severity,zillow_sale,zipCode,bedroom,'Athens')
                
        elif answer == '5':
                analyze.crimes_per_month(category_map)
                
        elif answer == '6':
                analyze.price_data(zillow_sale,zillow_rent)
                
        elif answer == '7':
            city = chooseCity()
            if city == '1':
                analyze.drawCityZipCode(category_map[category_map.City=='Pittsburgh'])
            elif city == '2':
                analyze.drawCityZipCode(category_map[category_map.City=='Madison'])
            elif city == '3':
                analyze.drawCityZipCode(category_map[category_map.City=='Buffalo'])
            elif city == '4':
                analyze.drawCityZipCode(category_map[category_map.City=='Athens'])

        elif answer == '8':
            city = chooseCity()
            bedroom = chooseBedRoom()
            if city == '1':
                analyze.plotAveragePropertyPrices(zillow_sale[zillow_sale.City=='Pittsburgh'])
                analyze.plotAverageRentPrices(zillow_rent[zillow_rent.City=='Pittsburgh'],bedroom)
            elif city == '2':
                analyze.plotAveragePropertyPrices(zillow_sale[zillow_sale.City=='Madison'])
                analyze.plotAverageRentPrices(zillow_rent[zillow_rent.City=='Pittsburgh'],bedroom)
            elif city == '3':
                analyze.plotAveragePropertyPrices(zillow_sale[zillow_sale.City=='Buffalo'])
                analyze.plotAverageRentPrices(zillow_rent[zillow_rent.City=='Pittsburgh'],bedroom)
            elif city == '4':
                analyze.plotAveragePropertyPrices(zillow_sale[zillow_sale.City=='Athens'])
                analyze.plotAverageRentPrices(zillow_rent[zillow_rent.City=='Pittsburgh'],bedroom)
        
        elif answer == '9':
            city = chooseCity()
            zipCode = chooseZip(zillow_rent,city)
            if city == '1':
                analyze.crimes_month(category_map,'Pittsburgh',zipCode)
            elif city == '2':
                analyze.crimes_month(category_map,'Madison',zipCode)
            elif city == '3':
                analyze.crimes_month(category_map,'Buffalo',zipCode)
            elif city == '4':
                analyze.crimes_month(category_map,'Athens',zipCode)
                
        elif answer == '10':
            city = chooseCity()
            zipCode = chooseZip(zillow_rent,city)
            if city == '1':
                analyze.sales_stats(zillow_sale,'Pittsburgh',zipCode)
            elif city == '2':
                analyze.sales_stats(zillow_sale,'Madison',zipCode)
            elif city == '3':
                analyze.sales_stats(zillow_sale,'Buffalo',zipCode)
            elif city == '4':
                analyze.sales_stats(zillow_sale,'Athens',zipCode)
                
        elif answer == '11':
            city = chooseCity()
            zipCode = chooseZip(zillow_rent,city)
            if city == '1':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '2':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '3':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
            elif city == '4':
                analyze.plotAverageRentPricesWithZip(zillow_rent,zipCode)
                
        elif answer == '12':
                analyze.crimes_by_city(category_map)
                
        elif answer == '13':
            city = chooseCity()
            zipCode = chooseZip(zillow_rent,city)
            if city == '1':
                analyze.crime_data(category_map,'Pittsburgh',zipCode)
            elif city == '2':
                analyze.crime_data(category_map,'Madison',zipCode)
            elif city == '3':
                analyze.crime_data(category_map,'Buffalo',zipCode)
            elif city == '4':
                analyze.crime_data(category_map,'Athens',zipCode)
                
    print('Thank you and Good Bye!')
            



    