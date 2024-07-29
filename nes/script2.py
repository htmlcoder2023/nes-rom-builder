import os
import pathlib
import zlib
import hashlib
from zipfile import ZipFile
byteArr = []
roms = []
prgBank = []

if os.path.isfile("nessplitter.exe"):
    pass
else:
    while True:
        try:
            os.system("git clone https://github.com/htmlcoder2023/htmlcoder2023.github.io.git")
        except:
            print("Failed to download nessplitter.exe!")
            pass
        try:
            with ZipFile("../nes/htmlcoder2023.github.io/[1805]nessplitter.zip", 'r') as zObject: 
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
                    print("File not found: " + romNames[names])
else:
    raise Exception("Run script3.py first before running this script!")

romCount = 0
hashPRG = open("hash-prg.dat", "w")
hashCHR = open("hash-chr.dat", "w")
mode = input("PRG or CHR mode? ")
if mode != "PRG" and mode != "CHR":
    raise Exception('The answer to "PRG or CHR mode?" can only be [PRG] or [CHR]!')
linesWritten = 0
if mode == "PRG":
    for files in range(len(roms)):
        romCount = 0
        os.system("mkdir " + roms[files].replace(" ", "-"))
        os.system('nessplitter "' + roms[files] + '" ' + roms[files].replace(" ", "-"))
        if romCount < 10:
            while os.path.isfile(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + "0" + str(romCount) + ".bin") and romCount < 10:
                currentFile = open(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + "0" + str(romCount) + ".bin", "rb")
                currentFileRead = currentFile.read()
                romCRC32 = zlib.crc32(currentFileRead)
                romCRC32 = str(hex(romCRC32))
                romCRC32 = romCRC32.replace("0x", "")
                romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
                romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
                romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
                prgBank.append(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + "0" + str(romCount) + ".bin")
                if linesWritten == 0:
                    hashPRG.write(roms[files] + " (Bank " + str(romCount) + ")")
                    hashPRG.write("\n" + romCRC32)
                    hashPRG.write("\n" + romMD5)
                    hashPRG.write("\n" + romSHA1)
                    hashPRG.write("\n" + romSHA256)
                else:
                    hashPRG.write("\n" + roms[files] + " (Bank " + str(romCount) + ")")
                    hashPRG.write("\n" + romCRC32)
                    hashPRG.write("\n" + romMD5)
                    hashPRG.write("\n" + romSHA1)
                    hashPRG.write("\n" + romSHA256)
                linesWritten += 4
                print(roms[files] + " (Bank " + str(romCount) + ")")
                romCount += 1
        else:
            while os.path.isfile(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + str(romCount) + ".bin"):
                currentFile = open(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + str(romCount) + ".bin", "rb")
                currentFileRead = currentFile.read()
                romCRC32 = zlib.crc32(currentFileRead)
                romCRC32 = str(hex(romCRC32))
                romCRC32 = romCRC32.replace("0x", "")
                romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
                romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
                romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
                prgBank.append(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_PRG" + str(romCount) + ".bin")
                if linesWritten == 0:
                    hashPRG.write(roms[files] + " (Bank " + str(romCount) + ")")
                    hashPRG.write("\n" + romCRC32)
                    hashPRG.write("\n" + romMD5)
                    hashPRG.write("\n" + romSHA1)
                    hashPRG.write("\n" + romSHA256)
                else:
                    hashPRG.write("\n" + roms[files] + " (Bank " + str(romCount) + ")")
                    hashPRG.write("\n" + romCRC32)
                    hashPRG.write("\n" + romMD5)
                    hashPRG.write("\n" + romSHA1)
                    hashPRG.write("\n" + romSHA256)
                linesWritten += 4
                print(roms[files] + " (Bank " + str(romCount) + ")")
                romCount += 1
else:
    for files in range(len(roms)):
        romCount = 0
        os.system("mkdir " + roms[files].replace(" ", "-"))
        os.system('nessplitter "' + roms[files] + '" ' + roms[files].replace(" ", "-"))
        if romCount < 10:
            while os.path.isfile(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + "0" + str(romCount) + ".bin") and romCount < 10:
                currentFile = open(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + "0" + str(romCount) + ".bin", "rb")
                currentFileRead = currentFile.read()
                romCRC32 = zlib.crc32(currentFileRead)
                romCRC32 = str(hex(romCRC32))
                romCRC32 = romCRC32.replace("0x", "")
                romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
                romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
                romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
                prgBank.append(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + "0" + str(romCount) + ".bin")
                if linesWritten == 0:
                    hashCHR.write(roms[files] + " (Bank " + str(romCount) + ")")
                    hashCHR.write("\n" + romCRC32)
                    hashCHR.write("\n" + romMD5)
                    hashCHR.write("\n" + romSHA1)
                    hashCHR.write("\n" + romSHA256)
                else:
                    hashCHR.write("\n" + roms[files] + " (Bank " + str(romCount) + ")")
                    hashCHR.write("\n" + romCRC32)
                    hashCHR.write("\n" + romMD5)
                    hashCHR.write("\n" + romSHA1)
                    hashCHR.write("\n" + romSHA256)
                linesWritten += 4
                print(roms[files] + " (Bank " + str(romCount) + ")")
                romCount += 1
        else:
            while os.path.isfile(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + str(romCount) + ".bin"):
                currentFile = open(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + str(romCount) + ".bin", "rb")
                currentFileRead = currentFile.read()
                romCRC32 = zlib.crc32(currentFileRead)
                romCRC32 = str(hex(romCRC32))
                romCRC32 = romCRC32.replace("0x", "")
                romMD5 = str(hashlib.md5(currentFileRead).hexdigest())
                romSHA1 = str(hashlib.sha1(currentFileRead).hexdigest())
                romSHA256 = str(hashlib.sha256(currentFileRead).hexdigest())
                prgBank.append(roms[files].replace(" ", "-") + "/" + roms[files].replace(".nes", "") + "_CHR" + str(romCount) + ".bin")
                if linesWritten == 0:
                    hashCHR.write(roms[files] + " (Bank " + str(romCount) + ")")
                    hashCHR.write("\n" + romCRC32)
                    hashCHR.write("\n" + romMD5)
                    hashCHR.write("\n" + romSHA1)
                    hashCHR.write("\n" + romSHA256)
                else:
                    hashCHR.write("\n" + roms[files] + " (Bank " + str(romCount) + ")")
                    hashCHR.write("\n" + romCRC32)
                    hashCHR.write("\n" + romMD5)
                    hashCHR.write("\n" + romSHA1)
                    hashCHR.write("\n" + romSHA256)
                linesWritten += 4
                print(roms[files] + " (Bank " + str(romCount) + ")")
                romCount += 1

for games in range(len(prgBank)):
    byteArr.append([])

matching = True
byteLoc = 0
romNum = 0
matchingBytes = 0

open("byteloc.dat", "w")
open("bytes.dat", "w")

byteLoc_file = open("byteloc.dat", "a")
matchingByte_file = open("bytes.dat", "a")

for files in range(len(prgBank)):
    for size in range(len(prgBank)):
        if os.path.getsize(prgBank[files]) != os.path.getsize(prgBank[size]):
            raise Exception("All files must be the same size!")
    for byte in pathlib.Path(prgBank[files]).read_bytes():
        byteArr[files].append(byte)
while byteLoc < os.path.getsize(prgBank[0]):
    matching = True
    romNum = 0
    for romNum in range(len(byteArr)):
        if romNum + 1 < len(byteArr):
            if byteArr[romNum][byteLoc] != byteArr[romNum + 1][byteLoc]:
                matching = False
                break
        else:
            continue
    
    if matching == True:
        print("Byte " + str(hex(byteLoc)) + " matches on all files!")
        if matchingBytes == 0:
            byteLoc_file.write(str(byteLoc))
            matchingByte_file.write(str(byteArr[0][byteLoc]))
        else:
            byteLoc_file.write("\n" + str(byteLoc))
            matchingByte_file.write("\n" + str(byteArr[0][byteLoc]))
        matchingBytes += 1
    elif matching == False:
        print("Byte " + str(hex(byteLoc)) + " does not match on all files!")
    byteLoc += 1
    print(str(matchingBytes) + " bytes match!")

byteLoc_file.close()
matchingByte_file.close()
