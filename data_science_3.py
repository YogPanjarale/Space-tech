
from data_science_2 import planet_typelist,planets
terrestrials_and_super_earths = []

for i in range(len(planets)):
    if planet_typelist[i]=="Super Earth" or planet_typelist[i]=="Terrestrial":
        terrestrials_and_super_earths.append(planets[i])
print(len(terrestrials_and_super_earths))
t=terrestrials_and_super_earths[:]
orbital_period_list=[]
orbital_radius_list=[]
for i in range(len(t)):
    p=t[i]
    isUnkown=False
    if p['orbital_radius'].lower()=='Unknown'.lower():
        terrestrials_and_super_earths.remove(p)
        isUnkown=True
    else:
        if not p['orbital_period'].endswith(' days'):
            ti=terrestrials_and_super_earths.index(p)
            valinit:str=terrestrials_and_super_earths[ti]['orbital_period']
            valint = float(valinit.removesuffix(' years'))
            valdays = valint*365
            terrestrials_and_super_earths[ti]['orbital_period']=f'{round(valdays,4)} days'
    if not isUnkown:
        _or=float(p['orbital_radius'].removesuffix(' AU'))
        _op=float(p['orbital_period'].removesuffix(' days'))
        if (_or<2 and _or>0.38): 
            orbital_radius_list.append(_or)
            orbital_period_list.append(_op)
print(len(terrestrials_and_super_earths))
print(terrestrials_and_super_earths[627])


if __name__=='__main__':
    from plotly.express import scatter
    title = f"Planets in Goldilocks Zone : {len(orbital_period_list)}"
    plot1 = scatter(x=orbital_radius_list,y=orbital_period_list,title=title)
    plot1.show()