import requests
import json
from types import SimpleNamespace

url="https://pokeapi.co/api/v2/pokemon/pikachu"
datos= requests.get(url)

x = json.loads(datos.text, object_hook=lambda d: SimpleNamespace(**d))

for a in x.abilities:
    print(a.ability.name)
