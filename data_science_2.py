'''
F = G (m1m2/r2)
'''
from data_science_1 import getPlanets
from pandas import DataFrame
from math import  exp
# planets = getPlanets('HD 10180')['planets']
planets = getPlanets()
# print(planets)
gravity_list = []
mass_list = []
radius_list=[]
name_list=[]
planet_typelist=[]
for p in planets:
    mass_list.append(float(p['mass']))
    radius_list.append(float(p['radius']))
    planet_typelist.append(str(p['planet_type']))
    name_list.append(str(p['name']))
# print(name_list,mass_list,radius_list)

for i in range(len(name_list)):
    mass = mass_list[i]
    radius = radius_list[i]
    name = name_list[i]

    gravity = abs(float(mass*exp(5.972) + 24) / float((radius**2)*(6371000**2)*exp(6.674)-11)) 
    gravity_list.append(gravity)
    # print(gravity)
# print(max(radius_list))
for i in range(len(radius_list)):
    if radius_list[i]==0:
        # print(name_list[i],mass_list[i],radius_list[i],gravity_list[i])
        print(planets[i])
        pass


lessthen10=[]
from10to100 = []

for g in gravity_list:
    if (g<100) and (g>10):
        from10to100.append(g)
    elif (g<=10):
        lessthen10.append(g)

print(f"Less Then 10 : {len(lessthen10)}")
print(f"10 to 100 : {len(from10to100)}")
print(set(planet_typelist))

if __name__ =="__main__":
    from plotly.express import scatter
    # frame = DataFrame({"radius":radius_list,"mass":mass_list,"name":name_list,"gravity":gravity_list,"hover_data_0":name_list})
    # plot  = scatter(x=radius_list,y=mass_list,size=gravity_list)
    # plot = scatter(frame,x="radius",y="mass",size="gravity",hover_data="name")
    # plot.show()
    plot1 = scatter(x=radius_list,y=mass_list)
    plot1.show()



l=[]
for i,m in enumerate(mass_list):
    
    tl=[radius_list[i],m]
    l.append(tl)


if __name__ =="__main__":
    import seaborn as sb
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    wcss =[]
    for i in range(1,11):
        t= KMeans(n_clusters=i,init='k-means++',random_state=33)
        t.fit(l)
    wcss.append(t.inertia_)
    plt.figure(figsize=(10,5))
    sb.lineplot(range(1,11),wcss,markers='o',color='orange')

    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

