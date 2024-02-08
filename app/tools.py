import requests as r
from .models import Pokemon
    
def poke_getter(id):
    res = r.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = res.json()
    name = data['name']
    if data['sprites']['other']['dream_world']:
        img = data['sprites']['other']['dream_world']['front_default']
    else:
        img = data['sprites']['front_shiny']
    species = data['species']['name']
    poke = Pokemon(name, img, species)
    poke.save_poke()
    return poke.to_dict()