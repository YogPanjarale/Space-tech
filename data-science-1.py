import csv

with open("data/given.csv","r") as f:
    r = csv.reader(f)
    rows = []
    for i in r:
        rows.append(i)
    headers = rows[0]
    planet_data_rows = rows[1:]
    # print(headers,"\n=========\n",planet_data_rows[0])
    planets_count = {}
    for p in planet_data_rows:
        if planets_count.get(p[11]):
            planets_count[p[11]]['count']+=1
            planets_count[p[11]]['planets'].append(p[1])


        else :
            planets_count[p[11]]={
                'count':1,
                'planets':[p[1]]
            }
    max_planet = max(planets_count,key=lambda x: planets_count[x]['count'])
    # print(max_planet)
    
    # hd_10180 = planets_count['hd 10180'.upper()]
    # print(hd_10180)
    print(len(planet_data_rows))
    temp_planet_data = list(planet_data_rows)
    for i in temp_planet_data:
        planet_mass:str = i[3]
        if planet_mass.lower()=="unknown":
            planet_data_rows.remove(i)
            continue
        else:
            remain = planet_mass.split(' ')[0]
            t2 = planet_mass.split(' ')[1]
            if t2 =="Jupiters":
                remain=float(remain)*317.8
                i[3]=remain
        planet_radius = i[7]
        if planet_radius.lower()=="unknown":
            planet_data_rows.remove(i)
            continue
        else:
            remain = planet_radius.split(' ')[0]
            t2 = planet_radius.split(' ')[2]
            if t2 =="Jupiter":
                remain=float(remain)*11.2
                i[7]=remain
    print(len(planet_data_rows))