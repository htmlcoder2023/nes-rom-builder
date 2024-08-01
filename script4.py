import os
from zipfile import ZipFile
import platform

romZip = input("What .zip file contains the zipped ROMs? ")
if os.path.isfile(romZip):

else:
    raise Exception("File not found!")
inputFile = input("What file contains the ROM hashes? ")
if os.path.isfile(inputFile):
    datFile = open(inputFile, "r")
else:
    raise Exception("File not found!")
games = []

while True:
    line = datFile.readline()
    if "(" in line:
        games.append(line)
    if not line:
        break

datFile.close()

inputDir = input("What is the current working directory? ")

if os.path.isfile("../" + inputDir + "/script4.py") or os.path.isfile("../" + inputDir + "/script4.exe"):
    continue
else:
    raise Exception("Directory not found!")

lines = 0
outputFile = input("Where will the database of NES rom versions be stored? ")
datFile = open(outputFile, "w")

with ZipFile("../" + inputDir + romZip, 'r') as zObject: 
    zObject.extractall(
        path="../" + inputDir
    )

writtenNum = 0

fileExtension_num = input("How many file extensions need to be replaced? ")

for lines in range(len(games)):
    games[lines] = games[lines].replace("\n", "")
    games[lines] = games[lines].replace("amp;", "")
    for thugs in range(fileExtension_num):
        fileExtension = input("Which file extension? ")
        games[lines] = games[lines].replace(fileExtension, ".zip")
    if os.path.isfile(games[lines]):
        games.pop(lines)
        lines -= 1
        continue
    else:
        try:
            with ZipFile("../" + inputDir + "/" + games[lines], "r") as zObject:
                zObject.extractall(
                    path="../" + inputDir
                )
        except:
            pass

    if writtenNum == 0:
        datFile.write(games[lines])
    else:
        datFile.write("\n" + games[lines])
    writtenNum += 1

datFile.close()
