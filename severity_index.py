# -*- coding: utf-8 -*-
"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed
          
This code categories and scores the crime based on their severity.
"""

def severity_index():
    # Import the required package    
    import pandas as pd
    
    # Read the required data into csv
    crime_data = pd.read_csv('category_mapped_crime_merged.csv') 
    
    # Dictionary for severity mapping
    severity_map = {
            "Theft": 1,
            "Sexual Abuse": 3,
            "Murder": 3,
            "Assault": 2,
            "Rape": 3,
            "Forgery": 1,
            "Vandalism": 1,
            "Accident": 1,
            "Traffic Accidents": 2,
            "Missing Person": 3,
            "Drug Abuse": 2,
            "Harassment": 2,
            "Trespassing": 1,
            "Threats": 1,
            "Weapon Violation": 2,
            "Suspicious Entity": 1,
            "Drinking in Public": 1,
            "Noise Complaint": 1,
            "Domestic Abuse": 3,
            "Animal Abuse": 1,
            "Child Abuse": 3,
            "Misconduct": 1,
            "Kidnapping": 3,
            "Stalking": 1,
            "Extortion": 2,
            "Indecent Exposure": 1,
            "Prostitution": 2,
            "Terrorism": 3,
            "Evidence Tampering": 2,
            "Others": 1
            }
    
    # Creating a column for Severity Index
    crime_data['Severity Index'] = None
    
    # Mapping severity index to original data set based on crime category 
    for row in range(len(crime_data)):
        crime_data['Severity Index'][row] = severity_map.get(crime_data['Crime Category'][row]) 
     
    # Writing the final dataframe to a csv file
    crime_data.to_csv('severity_category_mapped_crime.csv', index = False)
    return crime_data


