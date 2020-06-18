"""

Group 9 : Crime Patrol
Members: Tanvi Mittal
          Pooja Vasudevan
          Arkesh rath
          Syed Danish Ahmed
          
This code extracts the zipcode based on address.
"""

# Imports
from selenium import webdriver
import time

# Function to map address to zipcode
def zipExtractor(df_madison):
    driver = webdriver.Chrome('chromedriver.exe')
    url_zip = "https://tools.usps.com/zip-code-lookup.htm?byaddress"
    driver.get(url_zip)
    df500 = df_madison.head(500)
#    df500 = df_madison.head(10)
    df500['Zip'] =''
    for i in range(len(df500)):
        # Find the text field and enter a value
        street = driver.find_element_by_id("tAddress")
        street.send_keys(df_madison['Address'][i].replace('block','').replace('Block',''))
        city = driver.find_element_by_id("tCity")
        city.send_keys('Madison')
        state = driver.find_element_by_id("tState")
        state.send_keys('WI - Wisconsin')
        find = driver.find_element_by_id("zip-by-address")
        find.click()
        time.sleep(3)
        try:
            # Extract the zip value from the results
            zipcode = driver.find_element_by_xpath("(.//li[@class='list-group-item paginate'])[1]")
            temp= zipcode.text
            l = temp.split("\n")
            df500['Zip'][i] = l[1][-10:]
            df500['Zip'][i] = df500['Zip'][i][:5]
            next_zip = driver.find_element_by_id("search-address-again")
            next_zip.click()
        except:
            df500['Zip'][i] = 'Not found'
            # Clear the fields before use
            street.clear()
            city.clear()
            
    df500 = df500[df500.Zip != 'Not Found']
            
    dfcopy = df500.copy()
    dfcopy = dfcopy[dfcopy['Zip'].str.startswith('5')].reset_index()
    dfcopy['Zip'].unique()
    driver.quit()
    return dfcopy
    
