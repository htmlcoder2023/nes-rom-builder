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
    games[lines] = games[lines].replace(".unh", ".nes")
    datFile.write(games[lines])
    lines += 1
datFile.close()

lines = 0

for lines in range(len(games)):
    if os.path.isfile(games[lines]):
        games.pop(lines)
        continue
    else:
        games[lines] = games[lines].replace("(", "%28")
        games[lines] = games[lines].replace("\n", "")
        games[lines] = games[lines].replace(")", "%29")
        games[lines] = games[lines].replace(".bin", ".zip")
        games[lines] = games[lines].replace(".nes", ".zip")
        games[lines] = games[lines].replace(",", "%2C")
        games[lines] = games[lines].replace("[", "%5B")
        games[lines] = games[lines].replace("]", "%5D")
        games[lines] = games[lines].replace("&", "%26")
        games[lines] = games[lines].replace("+", "%2B")

while True:
    for lines in range(len(games)):
        while True:
            try:
                urllib.request.urlretrieve("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29/" + games[lines], games[lines])
            except:
                pass
            print("You have created " + str(lines + 1) + " files.")
            with ZipFile("../nes/" + games[lines], 'r') as zObject: 
                zObject.extractall(
                    path="../nes"
                )
            try:
                urllib.request.urlretrieve("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headerless%29/" + games[lines], games[lines])
            except:
                pass
            with ZipFile("../nes/" + games[lines], 'r') as zObject: 
                zObject.extractall(
                    path="../nes"
                )
            print(str(lines + 1) + " files extracted!")
            break
    break

os.system("del *.zip")
