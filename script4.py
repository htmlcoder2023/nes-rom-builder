import urllib.request
import os
from zipfile import ZipFile
import platform

inputFile = input("What file contains the ROM hashes? ")
datFile = open(inputFile, "r")
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

inputDir = input("What is the current working directory?" )

lines = 0
outputFile = input("Where will the database of NES rom versions be stored? ")
datFile = open(outputFile, "w")

if mode == "yes":
    if platform.system() == "Windows":
        os.system("move nes-roms.zip ..")
        os.system("del *.zip")
    else:
        os.system("chmod +w *.zip")
        os.system("mv nes-roms.zip ..")
        os.system("rm *.zip")

if extract == "yes":
    with ZipFile("../" + inputDir + "/nes-roms.zip", 'r') as zObject: 
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
                with ZipFile("../" + inputDir "/" + games[lines].replace(".nes", ".zip"), 'r') as zObject:
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
