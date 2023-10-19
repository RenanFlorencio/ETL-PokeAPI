import requests
import json

pokeapi_url = "https://pokeapi.co/api/v2/"

def req_pokemon(pokemon_name):
    response = requests.get(f'{pokeapi_url}/pokemon/{pokemon_name}') 
    return response.json() if response.status_code == 200 else None


pokemon_names = ['pikachu', 'gengar', 'butterfree']
infos = []

for pok in pokemon_names:
    response = req_pokemon(pok)
    if response != None:
        infos.append(response)


print(json.dumps(infos[0], indent=2))

