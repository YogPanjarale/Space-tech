import time,csv,os
from bs4 import BeautifulSoup
from selenium import webdriver

target_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
browser.get(target_url)
def scrape():
    headers =[
        "pageno",
        "name", 
        "light_years_from_earth", 
        "planet_mass", 
        "stellar_magnitude", 
        "discovery_date"
    ]
    planet_data = []
    for i in range(0,338):
        soup = BeautifulSoup(browser.page_source,"html.parser",)
        for ul_tag in soup.find_all("ul",attrs={"class":"exoplanet"}):
            li_tags:soup = ul_tag.find_all("li")
            temp_list = []
            li_tag:soup
            temp_list.append(str(i))
            # print(ul_tag)
            for index,li_tag in enumerate(li_tags):
                li_tag:soup
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
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