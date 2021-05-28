from flask.json import jsonify
from output_validation import habitable_planets
from flask import Flask,request
# print(habitable_planets[0].keys())

app = Flask(__name__)

@app.get('/all')
def allHabitablePlanets():
    return jsonify(habitable_planets)
@app.get('/planet')
def getPlanetByName():
    planetname = request.args.get('name','NotFound')
    print(planetname)
    planet = list(filter(lambda p: p['name'] == planetname, habitable_planets))
    return jsonify(planet if planet else "Planet Not Found")
if __name__ =='__main__':
    print(habitable_planets[0]['name'])
    a=list(filter(lambda p: p['name'] == 'GJ 667 C g', habitable_planets))
    print(a)
    app.run(host='0.0.0.0',debug=True)