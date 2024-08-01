import os
import pathlib
import zlib
import hashlib
from zipfile import ZipFile
import platform
byteArr = []
roms = []
prgBank = []
workingDir = input("What is the current working directory? ")

if os.path.isfile("../" + workingDir + "/script4.py") or os.path.isfile("../" + workingDir + "/script4.exe"):

else:
    raise Exception("Directory not found!")

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
            with ZipFile("htmlcoder2023.github.io/[1805]nessplitter.zip", 'r') as zObject: 
                zObject.extractall(
                    path="../" + workingDir
                )
            break
        except:
            print("Failed to extract [1805]nessplitter.zip!")
            pass

gamesfile = input("File with Games: ")

if os.path.isfile(gamesfile):
    with open(gamesfile) as f:
        romNames = [romNames.rstrip() for romNames in f]
        for names in range(len(romNames)):
            if romNames[names].isspace() == False:
                if os.path.isfile(romNames[names]):
                    roms.append(romNames[names])
                else:
                    print("File not found: " + romNames[names])
else:
    raise Exception("File does not exist!")

romCount = 0
mode = input("PRG or CHR mode? ")
if mode != "PRG" and mode != "CHR":
    raise Exception('The answer to "PRG or CHR mode?" can only be [PRG] or [CHR]!')

if mode == "PRG":
    hash_prg = input("What file do you want to store the PRG hash data? ")
    hashPRG = open(hash_prg, "w")
elif mode == "CHR":
    hash_chr = input("What file do you want to store the CHR hash data? ")
    hashCHR = open(hash_chr, "w")
linesWritten = 0
if mode == "PRG":
    for files in range(len(roms)):
        romCount = 0
        roms[files] = roms[files].replace(",", " and")
        os.system('ren "' + roms[files].replace(" and", ",") + '" "' + roms[files] + '"')
        roms[files] = roms[files].replace("&", "and")
        os.system('ren "' + roms[files].replace("and", "&") + '" "' + roms[files] + '"')
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
        roms[files] = roms[files].replace(",", " and")
        os.system('ren "' + roms[files].replace(" and", ",") + '" "' + roms[files] + '"')
        roms[files] = roms[files].replace("&", "and")
        os.system('ren "' + roms[files].replace("and", "&") + '" "' + roms[files] + '"')
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
    print(prgBank[games])
    byteArr.append([])

matching = True
byteLoc = 0
romNum = 0
matchingBytes = 0

if platform.system() == "Windows":
    os.system("del *.nes")
else:
    os.system("chmod +w *.nes")
    os.system("rm *.nes")

if platform.system() == "Windows":
    os.system("move nes-roms.zip ../..")
    os.system("del *.zip")
else:
    os.system("chmod +w *.zip")
    os.system("mv nes-roms.zip ../..")
    os.system("rm *.zip")

if mode == "CHR":
    byteloc_chr = input("What file do you want to store the matching byte locations for CHR-ROM data? ")
    bytes_chr = input("What file do you want to store the byte values for CHR-ROM data? ")
    open(byteloc_chr, "w")
    open(bytes_chr, "w")
elif mode == "PRG":
    byteloc_prg = input("What file do you want to store the matching byte locations for PRG-ROM data? ")
    bytes_prg = input("What file do you want to store the byte values for PRG-ROM data? ")
    open(byteloc_prg, "w")
    open(bytes_prg, "w")

if mode == "CHR":
    byteLoc_file = open(byteloc_chr, "a")
    matchingByte_file = open(bytes_chr, "a")
elif mode == "PRG":
    byteLoc_file = open(byteloc_prg, "a")
    matchingByte_file = open(bytes_prg, "a")

for files in range(len(prgBank)):
    print(prgBank[files])
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
