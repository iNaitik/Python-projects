import requests

API_KEY = "aaacbf55-44ee-408d-a720-570a48f8eade"
name = input("Enter player name: ")


search_url = "https://api.cricapi.com/v1/players"
info_url = "https://api.cricapi.com/v1/players_info"

params = {"apikey":API_KEY,"search":name}
response = requests.get(search_url,params=params)

if response.status_code == 200:
    data = response.json()
    player = data['data'][0]
    print("Player found!!")
    player_id = player["id"]
    x = input("Do you want me to fetch stats: ")
else:
    print("Error")


info_params = {"apikey":API_KEY,"id":player_id}
response = requests.get(info_url,params=info_params)

if response.status_code == 200:
    if x == "":
        info_data = response.json()
        player_info = info_data['data']
        print("\n📊 Player Information:")
        print(f"Name: {player_info['name']}")
        print(f"ID: {player_info['id']}")
        print(f"Role: {player_info.get('role', 'N/A')}")
        print(f"Batting Style: {player_info.get('battingStyle', 'N/A')}")
        print(f"Bowling Style: {player_info.get('bowlingStyle', 'N/A')}")
        print(f"Country: {player_info['country']}")
        print(f"Date of Birth: {player_info.get('dateOfBirth', 'N/A')}")


