import os
from zipfile import ZipFile
import platform

datFile = open("fds_roms.dat", "r")
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

with ZipFile("../fds/fds-roms.zip", 'r') as zObject: 
    zObject.extractall(
        path="../fds"
    )

writtenNum = 0

for lines in range(len(games)):
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace("amp;", "")
    games[lines] = games[lines].replace(".bin", ".zip")
    if os.path.isfile(games[lines]):
        games.pop(lines)
        lines -= 1
        continue
    else:
        try:
            with ZipFile("../fds/" + games[lines].replace(".fds", ".zip"), 'r') as zObject:
                zObject.extractall(
                    path="../fds"
                )
        except:
            pass

    if writtenNum == 0:
        datFile.write(games[lines])
    else:
        datFile.write("\n" + games[lines])
    writtenNum += 1

datFile.close()
