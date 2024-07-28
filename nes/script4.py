import urllib.request
import os
from zipfile import ZipFile
import platform
from urllib.parse import urlparse

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False

datFile = open("nes.dat", "r")
games = []
while True:
    line = datFile.readline()
    if "(" in line:
        games.append(line)
    if not line:
        break

datFile.close()

lines = 0
datFile = open("games.dat", "w")

if platform.system() == "Windows":
    os.system("del *.zip")
else:
    os.system("chmod +w *.zip")
    os.system("rm *.zip")

writtenNum = 0

for lines in range(len(games)):
    if os.path.isfile(games[lines]) or not uri_validator("https://myrient.erista.me/files/No-Intro/Nintendo%20-%20Nintendo%20Entertainment%20System%20%28Headered%29/" + games[lines]):
        games.pop(lines)
        lines -= 1
        continue
    else:
        if writtenNum == 0:
            datFile.write(games[lines])
        else:
            datFile.write("\n" + games[lines])
        writtenNum += 1

datFile.close()

for lines in range(len(games)):
    games[lines] = games[lines].replace("amp;", "")
    games[lines] = games[lines].replace("(", "%28")
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace(")", "%29")
    games[lines] = games[lines].replace(" ", "%20")
    games[lines] = games[lines].replace(".bin", ".zip")
    games[lines] = games[lines].replace(".unh", ".zip")
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
                print("Failed to download " + games[lines] + "!")
                pass
            try:
                with ZipFile("../nes/" + games[lines], 'r') as zObject: 
                    zObject.extractall(
                        path="../nes"
                    )
                break
            except:
                pass
        print(str(lines + 1) + " files extracted!")
    break
