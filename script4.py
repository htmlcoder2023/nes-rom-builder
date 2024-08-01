import os
from zipfile import ZipFile

romZip = input("What .zip file contains the zipped ROMs? ")
if os.path.isfile(romZip):
    print("")
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
    print("")
else:
    raise Exception("Directory not found!")

outputFile = input("Where will the database of NES rom versions be stored? ")
datFile = open(outputFile, "w")

with ZipFile("../" + inputDir + "/" + romZip, 'r') as zObject: 
    zObject.extractall(
        path="../" + inputDir
    )

fileExtension_input = input("What file extension to replace? ")
fileExtension_output = input("What file extension to use instead? ")
fileExtension = input("Which file extension to replace to .zip archive? ")

lines = 0

while lines < len(games):
    while True:
        games[lines] = games[lines].replace("\n", "")
        games[lines] = games[lines].replace("amp;", "")
        games[lines] = games[lines].replace(fileExtension, ".zip")
        if os.path.isfile(games[lines].replace(".zip", fileExtension)):
            games.pop(lines)
            break
        else:
            with ZipFile("../" + inputDir + "/" + games[lines], "r") as zObject:
                zObject.extractall(
                    path="../" + inputDir
                )

        if lines == 0:
            datFile.write(games[lines])
        else:
            datFile.write("\n" + games[lines])
        lines += 1
        break

datFile.close()
