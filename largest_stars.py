from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

options = Options()

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
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
            print(col_data.txt)
            dat = col_data.text.strip()
            print(dat)
            templist.append(dat)
        scrapped_data.append(templist)
    stars_dat = []
    for i in range(0,len(scrapped_data)):
        Star_names = scrapped_data[i][1]
        Distance = scrapped_data[i][3]
        Mass =scrapped_data [i][5]
        Radius = scrapped_data[i][6]
        Lum = scrapped_data[i][7]

        requiredat = [Star_names , Distance , Mass , Radius , Lum]
        stars_dat.append(requiredat)
    headers = ["starname" , "dist(ly)" , "mass(solar masses)" , "radius(solar radius)" , "luminosity(sular lumens)"]
    stardf = pd.DataFrame(stars_dat , columns=headers)
    stardf.to_csv('scrapp.csv' , index = True,index_label="id")
scrape()
