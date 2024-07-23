import urllib.request
import os
from zipfile import ZipFile
datFile = open("nes.dat", "r")
games = []
while True:
    line = datFile.readline()
    if "(" in line:
        games.append(line)
    if not line:
        break

datFile = open("games.dat", "w")
lines = 0
os.system("del *.nes")
os.system("del *.zip")
while lines < len(games):
    games[lines] = games[lines].replace("amp;", "")
    datFile.write(games[lines].replace(".unh", ".nes"))
    lines += 1
datFile.close()

lines = 0

for lines in range(len(games)):
    games[lines] = games[lines].replace("(", "%28")
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace(")", "%29")
    games[lines] = games[lines].replace(".unh", ".zip")
    games[lines] = games[lines].replace(",", "%2C")
    games[lines] = games[lines].replace(" ", "%20")
    games[lines] = games[lines].replace("[", "%5B")
    games[lines] = games[lines].replace("]", "%5D")
    games[lines] = games[lines].replace("&", "%26")
    games[lines] = games[lines].replace("+", "%2B")

while True:
    for lines in range(len(games)):
        try:
            urllib.request.urlretrieve("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29/" + games[lines], games[lines])
            print("You have created " + str(lines + 1) + " files.")
        except:
            print("Download failed.")
            continue
    break

  
with ZipFile("C:/Users/a19ro/Downloads/nes-rom-builder/*.zip", 'r') as zObject: 
    zObject.extractall(
        path="C:/Users/a19ro/Downloads/nes-rom-builder"
    )
    print(str(lines + 1) + " files have been extracted!")
    os.system("del " + games[lines])