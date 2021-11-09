from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def scrapeData ():
    START_URL = (
        "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
    )
    wiki = requests.get(START_URL)
    soup = BeautifulSoup(wiki.text, "html.parser")
    temp_list = []
    for tr in soup.find("table").find_all("tr"):
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    
    name = []
    distance = []
    distance = []
    mass = []
    radius = []
    
    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
    
    df = pd.DataFrame(
        list(zip(name, distance, mass, radius)),
        columns=["Star_name", "Distance", "Mass", "Radius"],
    )
    df.to_csv("data1.csv")


new_star_data = []

def scrape_more_data():
    url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.text,'html.parser')

    star_table = soup.find_all('table')
    print(len(star_table))

    temp_list= []
    table_rows = star_table[4].find_all('tr')
    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    print(len(temp_list))
    name = []
    distance = []
    mass = []
    radius = []
    
    for i in range(1, len(temp_list)):
        name.append(temp_list[i][0])
        distance.append(temp_list[i][5])
        mass.append(temp_list[i][8])
        radius.append(temp_list[i][9])
    
    df = pd.DataFrame(
        list(zip(name, distance, mass, radius)),
        columns=["Star_name", "Distance", "Mass", "Radius"],
    )
    df.to_csv("data2.csv")
scrape_more_data()    