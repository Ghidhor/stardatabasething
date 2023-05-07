from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import numpy as np
options = Options()

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
#brower = webdriver.Chrome("chromedriver.exe")
#brower.get(START_URL)

options.binary_location = "C:/Users/Kartoso/AppData/Local/Google/Chrome Dev/Application/chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r"chromedriver.exe")
driver.get(START_URL)
scrapped_data = []

def scrape():
    soup = BeautifulSoup(driver.page_source,"html.parser")
    brightest_stars  = soup.find("table",attrs = {"class","wikitable"})
    #print(brightest_stars)
    tab_bod = brightest_stars.find('tbody')
    tab_row = tab_bod.find_all('tr')
    #print("printing table rows",tab_row)
    for row in tab_row:
        #print(row)
        tab_colum = row.find_all('td')
        print("printing colum no :",tab_colum)
        templist = []
        for col_data in tab_colum:
            #print(col_data.txt)
            dat = col_data.text.strip()
            #print(dat)

            templist.append(dat)
        scrapped_data.append(templist)
    stars_dat = [] 
    #for row in stars_dat:
    #    replaced = []
    #    ## ADD CODE HERE ##
    #    for en in row:
    #        #en = en.replace("\n","")

    #        replaced.append(en)
    #    scrapped_data.append(replaced)
    for i in range(0,len(scrapped_data)):
        Star_names = scrapped_data[i][0]
        Distance = scrapped_data[i][5]
        Mass =scrapped_data [i][8]
        Radius =scrapped_data[i][9]
        #print("mass",Mass)
        #print("radius",Radius)
        #Mass = Mass*0.000954588
        #Radius = Radius*0.102763

        requiredat = [Star_names , Distance , Mass , Radius ]
        stars_dat.append(requiredat)
    headers = ["starname" , "dist(ly)" , "mass(suns)" , "radius(suns)"]
    stardf = pd.DataFrame(stars_dat , columns=headers)
    stardf['mass(suns)'].replace(regex=True, inplace=True, to_replace=r'[^0-9.]', value=r'')
    stardf['radius(suns)'].replace(regex=True, inplace=True, to_replace=r'[^0-9.]', value=r'')
    stardf['mass(suns)'].replace('', np.nan, inplace=True)
    stardf['radius(suns)'].replace('',np.nan , inplace = True)


    stardf2 = stardf.dropna()
    print("before",stardf2)
    stardf2 = stardf2.astype({'mass(suns)':float , 'radius(suns)':float})
    stardf2['mass(suns)'] =  stardf2['mass(suns)'] * 0.000954588
    stardf2['radius(suns)'] = stardf2['radius(suns)'] * 0.102763
    #stardf2.mul({'mass(suns)':0.000954588 , 'radius(suns)':0.102763})
    print("after" , stardf2)
    stardf2.to_csv('scrappp.csv' , index = True,index_label="id")
scrape()