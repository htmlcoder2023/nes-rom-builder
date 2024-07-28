import urllib.request
import os
from zipfile import ZipFile
import platform

datFile = open("nes.dat", "r")
games = []
mode = input("Download? ")
extract = input("Extract ROM Set? ")

if mode != "yes" and mode != "no":
    raise Exception("Mode can only be [yes] or [no]!")

if extract != "yes" and extract != "no":
    raise Exception('The answer to "Extract ROM Set?" can only be [yes] or [no]!')

if mode == "yes":
    extract = "no"

while True:
    line = datFile.readline()
    if "(" in line:
        games.append(line)
    if not line:
        break

datFile.close()

lines = 0
datFile = open("games.dat", "w")

if mode == "yes":
    if platform.system() == "Windows":
        os.system("move nes-roms.zip ..")
        os.system("del *.zip")
    else:
        os.system("chmod +w *.zip")
        os.system("mv nes-roms.zip ..")
        os.system("rm *.zip")

if extract == "yes":
    with ZipFile("../nes/nes-roms.zip", 'r') as zObject: 
        zObject.extractall(
            path="../nes"
        )

writtenNum = 0

for lines in range(len(games)):
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace("amp;", "")
    games[lines] = games[lines].replace(".unh", ".nes")
    if os.path.isfile(games[lines]):
        games.pop(lines)
        lines -= 1
        continue
    else:
        if extract == "yes":
            try:
                with ZipFile("../nes/" + games[lines].replace(".nes", ".zip"), 'r') as zObject:
                    zObject.extractall(
                        path="../nes"
                    )
            except:
                pass

    if writtenNum == 0:
        datFile.write(games[lines])
    else:
        datFile.write("\n" + games[lines])
    writtenNum += 1

datFile.close()

if mode == "yes":
    for lines in range(len(games)):
        games[lines] = games[lines].replace("(", "%28")
        games[lines] = games[lines].replace(")", "%29")
        games[lines] = games[lines].replace(" ", "%20")
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

if platform.system() == "Windows":
    os.system("move nes-roms.zip ..")
    os.system("del *.zip")
else:
    os.system("chmod +w *.zip")
    os.system("mv nes-roms.zip ..")
    os.system("rm *.zip")
