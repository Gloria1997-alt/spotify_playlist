import requests
from bs4 import BeautifulSoup


BASE_URL="https://www.billboard.com/charts/hot-100/"

date_of_songs=input("Which year do you want to travel to ?Type Date in this format: YYYY-MM-DD: ")

response = requests.get(BASE_URL+date_of_songs+"/")

contents=response.text

soup= BeautifulSoup(contents, 'html.parser')

songs = soup.find_all(name="h3", class_="a-no-trucate")
song_names = [sub.getText().strip() for sub in songs]
song = song_names[:: -1]

with open("songs.txt", mode="w") as file:
    for sub in song:
        file.write(f"{sub}\n")


