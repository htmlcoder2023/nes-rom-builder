import urllib.request
import os
from zipfile import ZipFile
datFile = open("fds.dat", "r")
games = []
while True:
    line = datFile.readline()
    if "(" in line:
        games.append(line)
    if not line:
        break

datFile = open("games.dat", "w")
lines = 0
os.system("del *.fds")
os.system("del *.bin")
os.system("del *.zip")
while lines < len(games):
    games[lines] = games[lines].replace("amp;", "")
    datFile.write(games[lines])
    lines += 1
datFile.close()

lines = 0

for lines in range(len(games)):
    games[lines] = games[lines].replace("(", "%28")
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace(")", "%29")
    games[lines] = games[lines].replace(" ", "%20")
    games[lines] = games[lines].replace(".bin", ".zip")
    games[lines] = games[lines].replace(".fds", ".zip")
    games[lines] = games[lines].replace(",", "%2C")
    games[lines] = games[lines].replace("[", "%5B")
    games[lines] = games[lines].replace("]", "%5D")
    games[lines] = games[lines].replace("&", "%26")
    games[lines] = games[lines].replace("+", "%2B")

while True:
    for lines in range(len(games)):
        while True:
            try:
                urllib.request.urlretrieve("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Family%20Computer%20Disk%20System%20%28FDS%29/" + games[lines], games[lines])
            except:
                print("Failed to download " + games[lines] + "!")
                pass
            try:
                with ZipFile("../fds/" + games[lines], 'r') as zObject: 
                    zObject.extractall(
                        path="../fds"
                    )
                break
            except:
                pass
        print(str(lines + 1) + " files extracted!")
    break

os.system("del *.zip")