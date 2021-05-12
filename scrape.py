import time,csv,os
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

target_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
browser.get(target_url)
final_list = []
planet_data = []
# planetTempData=[]
def getPlanetData(hyperlink:str):
    r =requests.get("https://exoplanets.nasa.gov"+hyperlink)
    soup = BeautifulSoup(r.content,"html.parser")
    planetTempData = []
    tr:soup
    tm ={}
    for tr in soup.find_all("tr",attrs={"class":"fact_row"}):
        td:soup = tr.find_all("td")
        temp_list = []
        for i in td:
            try:
                planetTempData.append(i.find_all("div",attrs={"class":"value"})[0].contents[0].replace("\n",""))
            except:
                planetTempData.append([])
    print(planetTempData)
    return planetTempData
        

headers= []
def scrape():
    headers =[
        "name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyperlink","planet_type","discovery_date","planet_mass","planet_radius","orbital_radius","orbital_period","eccentricity"
    ]
    
    for i in range(0,1):
        soup = BeautifulSoup(browser.page_source,"html.parser",)
        for ul_tag in soup.find_all("ul",attrs={"class":"exoplanet"}):
            li_tags:soup = ul_tag.find_all("li")
            temp_list = []
            li_tag:soup
            # print(ul_tag)
            href=""
            for index,li_tag in enumerate(li_tags):
                li_tag:soup
                if index==0:
                    d:soup =li_tag.find_all("a")[0]
                    temp_list.append(d.contents[0])
                    href=d.attrs["href"]
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            temp_list.append("https://exoplanets.nasa.gov"+href)
            t=getPlanetData(href)
            for i in t:
                    temp_list.append(i)
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        with open("planet_data.csv","w") as f:
            w = csv.writer(f)
            w.writerow(headers)
            w.writerows(planet_data)
            f.close()
if __name__=="__main__":
    print("Scraping ...")
    # f
    scrape()