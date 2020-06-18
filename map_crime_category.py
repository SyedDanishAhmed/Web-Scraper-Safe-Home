# -*- coding: utf-8 -*-
"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh Rath
          Syed Danish Ahmed
          
This code categorizes specific crime into general categories.
"""


import pandas as pd
import operator

def map_crime_category():
    
    # Reading data for all cities
    crime_merged_all_cities = pd.read_csv('crime_merged_all_cities.csv') 
    
    # Assigning it to a another data frame
    df = crime_merged_all_cities
    
    # Creating a dictionery for mapping the entities
    # The key represents the major Crime Categories that we have created manually
    # by going through all the unique Incident Types in all cities
    # The values in the dictionery are the possible keywords corresponding to each category 
    entity_map = {
            "Theft": ["theft", "larceny", "burglary", "robbery", "shoplifting", "break", "battery", "steal", "stole"],
            "Sexual Abuse": ["sex"],
            "Murder": ["murder", "homicide", "manslaughter"],
            "Assault": ["assault", "fight", "beat", "strangulation"],
            "Rape": ["rape"],
            "Forgery": ["forgery", "flim flam", "counterfeit", "embezzlement", "deception", "financial", "imperson"],
            "Vandalism":["vandalism", "property", "destruct"],
            "Accident":["accident", "injur"],
            "Traffic Accidents": ["traffic", "driv"],
            "Missing Person": ["missing"],
            "Drug Abuse": ["drug", "marijuana", "control"],
            "Harassment": ["harassment", "intimidat"],
            "Trespassing": ["trespass", "unwanted"],
            "Threats": ["threat"],
            "Weapon Violation": ["weapon", "firearm"],
            "Suspicious Entity": ["suspicio"],
            "Drinking in Public": ["drinkin", "liquor", "wine", "intoxi", "drunk"],
            "Noise Complaint": ["noise"],
            "Domestic Abuse": ["domestic", "family"],
            "Animal Abuse": ["animal"],
            "Child Abuse": ["child"],
            "Misconduct": ["misconduct","annoy", "accost", "obstruct"],
            "Kidnapping": ["kidnap"],
            "Stalking": ["stalk", "spy", "loiter", "prowl"],
            "Extortion": ["extort", "blackmail"],
            "Indecent Exposure": ["indecent", "exposure"],
            "Prostitution": ["prostitu"],
            "Terrorism": ["terror"],
            "Evidence Tampering":["tamper", "evidence"]        
            }
    
    # This dictionery maintains a score for every keyword match corresponding to each category
    # The category containing the highest matched score is selected 
    entity_score = {
            "Theft": 0,
            "Sexual Abuse": 0,
            "Murder": 0,
            "Assault": 0,
            "Rape": 0,
            "Forgery": 0,
            "Vandalism": 0,
            "Accident": 0,
            "Traffic Accidents": 0,
            "Missing Person": 0,
            "Drug Abuse": 0,
            "Harassment": 0,
            "Trespassing": 0,
            "Threats": 0,
            "Weapon Violation": 0,
            "Suspicious Entity": 0,
            "Drinking in Public": 0,
            "Noise Complaint": 0,
            "Domestic Abuse": 0,
            "Animal Abuse": 0,
            "Child Abuse": 0,
            "Misconduct": 0,
            "Kidnapping": 0,
            "Stalking": 0,
            "Extortion": 0,
            "Indecent Exposure": 0,
            "Prostitution": 0,
            "Terrorism": 0,
            "Evidence Tampering": 0
            }
    
    # Creating a new column in the dataframe
    df['Crime Category'] = None
    
    df['Incident Type'] = df['Incident Type'].str.lower()
    
    # Going through each row in the dataframe and matching the incident type to each of the categories
    # Entity score is upddated for each match
    # Category corresponding to the maximum score is considered the final category    
    for row in range(len(df)):
        entity_score = dict.fromkeys(entity_score, 0)
        for category in entity_map.keys():
            for keyword in entity_map[category]:
                if keyword in df['Incident Type'][row]:       
                    entity_score[category] += 1
        if max(entity_score.values()) > 0:
            df['Crime Category'][row] = max(entity_score.items(), key=operator.itemgetter(1))[0]
        else:
            df['Crime Category'][row] = "Others"
    
        
    # Writing the updated dataframe to a csv file
    df.to_csv('category_mapped_crime_merged.csv', index = False)
    return df