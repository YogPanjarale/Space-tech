import csv
import plotly.express as px
import re


def getPlanets():
    with open("data/given.csv", "r") as f:
        r = csv.reader(f)
        rows = []
        for i in r:
            rows.append(i)
        headers = rows[0]
        planet_data_rows = rows[1:]
        # print(len(planet_data_rows))
        temp_planet_data = list(planet_data_rows)
        for i in temp_planet_data:
            planet_mass: str = i[3]
            if planet_mass.lower() == "unknown":
                planet_data_rows.remove(i)
                continue
            else:
                remain = planet_mass.split(" ")[0]
                t2 = planet_mass.split(" ")[1]
                if t2 == "Jupiters":
                    remain = round(float(remain) * 317.8, 1)
                    i[3] = f"{remain} Earths"
            planet_radius = i[7]
            if planet_radius.lower() == "unknown":
                planet_data_rows.remove(i)
                continue
            else:
                remain = planet_radius.split(" ")[0]
                t2 = planet_radius.split(" ")[2]
                if t2 == "Jupiter":
                    remain = round(float(remain) * 11.2, 4)
                    i[7] = f"{remain} Earths"
        # print(len(planet_data_rows))
        # print(headers,"\n=========\n",planet_data_rows[0])
        planets_count = {}
        for p in planet_data_rows:
            if planets_count.get(p[11]):
                planets_count[p[11]]["count"] += 1
                planets_count[p[11]]["planets"].append(
                    {
                        "name": p[1],
                        "mass": p[3],
                        "radius": p[7],
                        "planet_type": p[6],
                        "orbital_radius": p[8],
                        "orbital_period": p[9],
                    }
                )

            else:
                planets_count[p[11]] = {
                    "count": 1,
                    "planets": [
                        {
                            "name": p[1],
                            "mass": p[3],
                            "radius": p[7],
                            "planet_type": p[6],
                            "orbital_radius": p[8],
                            "orbital_period": p[9],
                        },
                    ],
                }
        max_planet = max(planets_count, key=lambda x: planets_count[x]["count"])
        # print(max_planet)

        # hd_10180 = planets_count['hd 10180'.upper()]
        # print(hd_10180)
        # hd10180  = planets_count['HD 10180']
        # hd10180  = planets_count[star.upper()]
        # print(hd10180)
        # hd10180planetmass = []
        # hd10180planetname = []
        # for i in hd10180['planets']:
        #     hd10180planetname.append(i['name'])
        #     hd10180planetmass.append(float(i['mass'].replace(" Earths","")))
        # print(hd10180planetname,hd10180planetmass)
        # chart = px.bar(x=hd10180planetname,y=hd10180planetmass,labels=["Name","Mass"])
        # chart.show()
        planets = []
        t = []
        for star in planets_count.values():
            t.append(star["planets"])
        for p in t:
            for i in p:
                tm = i
                tm["mass"] = re.search("[0-9]+", i["mass"]).group()
                tm["radius"] = re.search("[0-9]+", i["radius"]).group()
                if tm["mass"] != "0" and tm["radius"] != "0":
                    # print(i,tm)
                    planets.append(tm)

        # print(planets)
        print("===========================")
        # print(hd10180)
        return planets


if __name__ == "__main__":
    r = getPlanets("HD 10180")
    # print(r)
