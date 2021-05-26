
mass=1
radius= 1
# gravity = abs(mass*float('5.972e+24') / float((radius**2)*(6371000**2)*float('6.674e-11')))
G=float('6.67408e-11')
gravity = G*(mass*float('5.972e+24'))  / ((radius**2)*(6371000**2))
print(gravity)