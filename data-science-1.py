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
    # planets_in_star ={}
    for p in planet_data_rows:
        if planets_count.get(p[11]):
            # planets_in_star[p[11]].append(p[1])
            planets_count[p[11]]+=1
        else:
            # planets[p[11]]={
            #     'planets':[p[11]],
            #     'count':1
            # }
            # planets_in_star[p[11]]=[p[1]]
            planets_count[p[11]]=1
    print(planets_count)
    max_planet = max(planets_count,lambda x: planets_count[x])
    print(max_planet)
    # print(max_planet)
    # print(planets[max_planet])

    # hd_10180 = planets_in_star['hd 10180'.upper()]
    # print(hd_10180)

    l =[]
    #getting from one planet data
    for i in planet_data_rows:
        pass