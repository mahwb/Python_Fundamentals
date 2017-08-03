import requests

r = requests.get('http://pokeapi.co/api/v2/pokemon/150')

#storing json response into variable to access
data = r.json()

print data["name"]