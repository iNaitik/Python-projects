import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Data not retrieved")

pokemon_name = input("Enter pokemon name: ")
pokemon_info = get_pokemon_info(pokemon_name)
typ = []
if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    for i in pokemon_info['types']:
        typ.append(i['type']['name'])
    print(f"Types:" ,", ".join(typ))

    #requests.get() is a Python function that accepts arguments like:
    #requests.get(url, params=..., headers=..., data=...)
