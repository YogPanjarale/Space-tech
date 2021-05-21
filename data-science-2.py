'''
F = G (m1m2/r2)
'''
from data_science_1 import getPlanets
from math import e
planets = getPlanets('HD 10180')['planets']
# print(planets)
gravity = []
mass_list = []
radius_list=[]
name_list=[]
for p in planets:
    mass_list.append(float(p['mass'].replace(" Earths","")))
    radius_list.append(float(p['radius'].replace(" Earths","")))
    name_list.append(p['name'])
# print(name_list,mass_list,radius_list)

for i in range(len(name_list)):
    mass = mass_list[i]
    radius = radius_list[i]
    name = name_list[i]

    gravity = (float(mass*(5.972*e) + 24) / float((radius**2)*(6371000**2)*(6.674*e)-11)) 
    print(gravity)