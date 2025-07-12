import requests
from datetime import datetime
from art import *

tprint("chess broker",font="random")
print("Created by linuxuser-hash")
username = input("\nVeuillez mettre le nom de votre cible : ").strip().lower()
url = f"https://api.chess.com/pub/player/{username}"
url2 = f"https://www.chess.com/callback/recover-password-data/{username}"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Referer": "https://www.chess.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie": "visitorid=%3A333d%3Affff%3A88.122.200.125",
}
response = requests.get(url,url2,headers=headers)
response2 = requests.get(url2,headers=headers)
data = response.json()
joined = data.get('joined')
last_online = data.get('last_online')
if last_online:
    lastonline = datetime.fromtimestamp(last_online).strftime('%d/%m/%Y')
if joined:
    date_joined = datetime.fromtimestamp(joined).strftime('%d/%m/%Y')
    

if response.status_code == 200:
    data2 = response2.json()
    print(f"Other : {data2}")
    print(f"\nNom d'utilisateur : {data.get('username')}")
    print(f"Country : {data.get('country')}")
    print(f"Avatar : {data.get('avatar')}")
    print(f"joined : {date_joined}")
    print(f"Status : {data.get('status')}")
    print(f"Is verified : {data.get('verified')}")
    print(f"Name : {data.get('name')}")
    print(f"Platform : {data.get('streaming_platforms')}")
    print(f"Location : {data.get('location')}")
    print(f"Player id : {data.get('player_id')}")
    print(f"League : {data.get('league')}")
    print(f"Followers : {data.get('followers')}")
    print(f"Last online : {lastonline}")
else:
       print(f"Erreur HTTP {response.status_code} ou utilisateur non trouvé.")
