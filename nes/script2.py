import os
import pathlib
import zlib
import hashlib
from zipfile import ZipFile
import platform
byteArr = []
roms = []
prgBank = []

if os.path.isfile("nessplitter.exe"):
    pass
else:
    while True:
        try:
            os.system("git clone https://github.com/htmlcoder2023/htmlcoder2023.github.io.git")
            os.system("move [1805]nessplitter.zip ..")
            if platform.system() == "Windows":   
                os.system("del htmlcoder2023.github.io")
            else:
                os.system("chmod +w htmlcoder2023.github.io")
                os.system("rm -rf htmlcoder2023.github.io")
        except:
            print("Failed to download nessplitter.exe!")
            pass
        try:
            with ZipFile("../nes/[1805]nessplitter.zip", 'r') as zObject: 
                zObject.extractall(
                    path="../nes"
                )
            break
        except:
            print("Failed to extract [1805]nessplitter.zip!")
            pass

if os.path.isfile("games.dat"):
    with open("games.dat") as f:
        romNames = [romNames.rstrip() for romNames in f]
        for names in range(len(romNames)):
            if romNames[names].isspace() == False:
                if os.path.isfile(romNames[names]):
                    roms.append(romNames[names])
                else:
                    raise Exception("You must have dumps of all of the ROMs in games.dat for this script to compare ROMs!")
else:
    raise Exception("Run script3.py first before running this script!")

numOfRoms = 0
romCount = 0
hashPRG = open("hash-prg.dat", "w")
hashCHR = open("hash-chr.dat", "w")
mode = input("PRG or CHR mode? ")
if mode != "PRG" or mode != "CHR":
    raise Exception('The answer to "PRG or CHR mode?" can only be [PRG] or [CHR]!')
linesWritten = 0

for files in range(len(roms)):
    romCount = 0
    os.system("mkdir " + roms[files].replace(" ", "-"))
    os.system("ren " + roms[files] + " " + roms[files].replace(" ", "-"))
    os.system("nessplitter " + roms[files].replace(" ", "-") + " " + roms[files].replace(" ", "-"))
    if romCount < 10:
        while os.path.isfile(roms[files].replace(" ", "-") + "_PRG" + "0" + str(romCount) + ".bin"):
            romCount += 1
            numOfRoms += 1
            currentFile = open(roms[files].replace(" ", "-") + "_PRG" + "0" + str(romCount) + ".bin", "rb")
            currentFileRead = currentFile.read()
            romCRC32 = zlib.crc32(currentFileRead)
            romCRC32 = str(hex(romCRC32))
            romCRC32 = romCRC32.replace("0x", "")
            romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
            romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
            romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
            if linesWritten == 0:
                hashPRG.write(roms[files])
                hashPRG.write("\n" + romCRC32)
                hashPRG.write("\n" + romMD5)
                hashPRG.write("\n" + romSHA1)
                hashPRG.write("\n" + romSHA256)
            else:
                hashPRG.write("\n" + roms[files])
                hashPRG.write("\n" + romCRC32)
                hashPRG.write("\n" + romMD5)
                hashPRG.write("\n" + romSHA1)
                hashPRG.write("\n" + romSHA256)
            linesWritten += 4
            continue
    else:
        while os.path.isfile(roms[files].replace(" ", "-") + "/" + roms[files].replace(" ", "-") + "_PRG" + str(romCount) + ".bin"):
            romCount += 1
            numOfRoms += 1
            currentFile = open(roms[files].replace(" ", "-") + "/" + roms[files].replace(" ", "-") + "_PRG" + str(romCount) + ".bin", "rb")
            currentFileRead = currentFile.read()
            romCRC32 = zlib.crc32(currentFileRead)
            romCRC32 = str(hex(romCRC32))
            romCRC32 = romCRC32.replace("0x", "")
            romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
            romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
            romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
            prgBank.append(roms[files].replace(" ", "-") + "/" + roms[files].replace(" ", "-") + "_PRG" + str(romCount) + ".bin")
            if linesWritten == 0:
                hashPRG.write(roms[files])
                hashPRG.write("\n" + romCRC32)
                hashPRG.write("\n" + romMD5)
                hashPRG.write("\n" + romSHA1)
                hashPRG.write("\n" + romSHA256)
            else:
                hashPRG.write("\n" + roms[files])
                hashPRG.write("\n" + romCRC32)
                hashPRG.write("\n" + romMD5)
                hashPRG.write("\n" + romSHA1)
                hashPRG.write("\n" + romSHA256)
            linesWritten += 4
            continue

for games in range(numOfRoms):
    byteArr.append([])

matching = True
byteLoc = 0
romNum = 0
matchingBytes = 0

open("byteloc.dat", "w")
open("bytes.dat", "w")

byteLoc_file = open("byteloc.dat", "a")
matchingByte_file = open("bytes.dat", "a")

romCount = 0
for files in range(len(prgBank)):
    for size in range(len(prgBank)):
        if os.path.getsize(prgBank[files]) != os.path.getsize(prgBank[size]):
            raise Exception("All files must be the same size!")
    for byte in pathlib.Path(prgBank[size]).read_bytes():
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