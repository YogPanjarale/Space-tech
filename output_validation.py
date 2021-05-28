'''
planets that are habitable based on 
1.Gravity <100, 
2.type is teristiral or super earth,
3.In Goldilock Zone, 
4.Speed less than 200
'''
from data_science_4 import terrestrials_and_super_earths
from data_science_2 import gravity_list,planets
# print(len(terrestrials_and_super_earths),len(gravity_list),len(planets))
# print(terrestrials_and_super_earths[0])
habitable_planets = []

for p in terrestrials_and_super_earths:
    #terrestrials_and_super_earths checked
    if p['gravity']<100 and p['in_goldilocks_zone'] ==True and  p['speed']<200 :
        habitable_planets.append(p)
if __name__=='__main__':
    print(len(habitable_planets))
    print(habitable_planets[0])