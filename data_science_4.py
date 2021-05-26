from math import e, exp, pi
from re import S
from data_science_3 import terrestrials_and_super_earths
# terrestrials_and_super_earths=terrestrials_and_super_earths[:10]
def convert():
    for p in terrestrials_and_super_earths:
        i = terrestrials_and_super_earths.index(p)
        op:str = p['orbital_period']
        op = float(op.removesuffix(' days'))
        #orbital period in days 
        # 1 day -> 86400 seconds
        # op = op*86400
        terrestrials_and_super_earths[i]['orbital_period']=op
        orb:str = p['orbital_radius']
        orb = float(orb.removesuffix(' AU'))
        # orbital_radius in AU
        # 1 AU -> 1.496e+8
        # orb  = orb * float('1.496e+8')
        terrestrials_and_super_earths[i]['orbital_radius']=orb
        # speed = dist/time
        # circum = 2*pi*float(orb)
        # circum = orb
        # speed = float(circum)/float(op)
        # print(circum)
        terrestrials_and_super_earths[i]['speed']= calculateSpeed(orb,op)

        # print(op,orb)
def removeGreaterThan(n:int=200):
    for p in terrestrials_and_super_earths:
        # print(float(str(p['speed'])))
        s = p['speed']
        # s=("%.17f" % s).rstrip('0').rstrip('.')
        # print(s)
        if s>200:
            terrestrials_and_super_earths.remove(p)

def calculateSpeed(oraduis,op):
    orb=oraduis
    orb  = orb * float('1.496e+8')
    # orb=s=("%.17f" % orb).rstrip('0').rstrip('.')
    op = op*86400
    circum = 2*pi*float(orb)
    speed = float(circum)/float(op)
    # print(speed,circum,op,orb,oraduis)
    return speed
    pass
convert()
if __name__=='__main__':
    s=calculateSpeed(1,365)
    # convert()
    removeGreaterThan(200)
    print(len(terrestrials_and_super_earths))