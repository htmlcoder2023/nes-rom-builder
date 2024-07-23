import os
import pathlib
byteArr = []
numOfRoms = int(input("How many ROMs will this script compare? "))
for games in range(numOfRoms):
    byteArr.append([])
roms = []

if os.path.isfile("games.dat"):
    with open("games.dat") as f:
        romNames = [romNames.rstrip() for romNames in f]
        for roms in range(len(romNames)):
            roms.append(romNames[roms])

matching = True
byteLoc = 0
romNum = 0
matchingBytes = 0

open("byteloc.dat", "w")
open("bytes.dat", "w")

byteLoc_file = open("byteloc.dat", "a")
matchingByte_file = open("bytes.dat", "a")

for files in range(len(roms)):
    for size in range(len(roms)):
        if os.path.getsize(roms[files]) != os.path.getsize(roms[size]):
            raise Exception("All files must be the same size!")
    for byte in pathlib.Path(roms[files]).read_bytes():
        byteArr[files].append(byte)
while byteLoc < os.path.getsize(roms[0]):
    romNum = 0
    matching = True
    while romNum < numOfRoms - 1:
        if byteArr[romNum][byteLoc] != byteArr[romNum + 1][byteLoc]:
            matching = False
            break
        romNum += 1
    
    if matching == True:
        print("Byte " + str(hex(byteLoc)) + " matches on all files!")
        if byteLoc < 16:
            input(str(hex(byteLoc)))
        else:
            if matchingBytes == 0:
                byteLoc_file.write(str(byteLoc))
                matchingByte_file.write(str(byteArr[romNum][byteLoc]))
            else:
                byteLoc_file.write("\n" + str(byteLoc))
                matchingByte_file.write("\n" + str(byteArr[romNum][byteLoc]))
            matchingBytes += 1
    elif matching == False:
        print("Byte " + str(hex(byteLoc)) + " does not match on all files!")
        if byteLoc < 16:
            input(str(hex(byteLoc)))

    byteLoc += 1
    print(str(matchingBytes) + " bytes match!")

byteLoc_file.close()
matchingByte_file.close()