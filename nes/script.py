# Thanks to @ranman for the response at https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
# And @CrouZ for the response at https://stackoverflow.com/questions/1742866/compute-crc-of-file-in-python

import random
import sys
from sys import platform
if sys.platform.startswith('win32'):
    system = "windows"
elif sys.platform.startswith('linux'):
    system = "linux"
    os.system("chmod +w *.bin")
import os.path
import os
import hashlib
import zlib
sys.set_int_max_str_digits(0)
satisfied = False
i = 0
sameBytes = []
bytesLoc = []

if os.path.isfile('bytes.dat') and os.path.isfile('byteloc.dat'):
    with open('bytes.dat') as f:
        lines = [line.rstrip() for line in f]
        for bytes in range(len(lines)):
            if lines[bytes].isspace() == False:
                sameBytes.append(int(lines[bytes]))
        f.close()

    with open('byteloc.dat') as f:
        loc = [loc.rstrip() for loc in f]
        for bytes in range(len(loc)):
            if loc[bytes].isspace() == False:
                bytesLoc.append(int(loc[bytes]) - 16)
        f.close()

registeredGames = 0
gameName = []
crc_LSS = []
md5_LSS = []
sha1_LSS = []
sha256_LSS = []

mode = 0

if os.path.isfile('nes.dat'):
    with open('nes.dat') as f:
        gameNames = [gameNames.rstrip() for gameNames in f]
        for games in range(len(gameNames)):
            if mode == 0:
                gameName.append(gameNames[games])
                mode += 1
            elif mode == 1:
                crc_LSS.append(gameNames[games])
                mode += 1
            elif mode == 2:
                md5_LSS.append(gameNames[games])
                mode += 1
            elif mode == 3:
                sha1_LSS.append(gameNames[games])
                mode += 1
            elif mode == 4:
                sha256_LSS.append(gameNames[games])
                mode = 0
            registeredGames += 1
        f.close()

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
numStop = int(input("How large is the .nes file without the header? "))

def crc32(fileName):
    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(numStop)
            if not s:
                break
            hash = zlib.crc32(s, hash)
        return "%08X" % (hash & 0xFFFFFFFF)

def md5_GEN(fileName):
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(numStop)
            if not data:
                break
            md5.update(data)
        return "MD5: {0}".format(md5.hexdigest())
        
def sha1_GEN(fileName):
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(numStop)
            if not data:
                break
            sha1.update(data)
        return "SHA1: {0}".format(sha1.hexdigest())
        
def sha256_GEN(fileName):
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(numStop)
            if not data:
                break
            sha256.update(data)
        return "SHA256: {0}".format(sha256.hexdigest())

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
 
    if power % 2 != 0:
        result = result * val
    return result

possibilities = optimize(256, numStop - len(bytesLoc))
if system == "windows":
    input("You are attempting to add " + str(possibilities) + " files. Are you sure about this? ")

while satisfied == False and i < possibilities:
    if system == "windows":
        os.system("del *.bin")
    elif system == "linux":
        os.system("rm *.bin")

    prg = open("file" + str(i + 1) + ".bin", "wb")

    bytesArr = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF]
    bytesWritten = 0
    prgCounter = 0
    finish = False

    while bytesWritten < numStop:
        if len(sameBytes) > 0 and bytesWritten == bytesLoc[prgCounter] and finish == False:
            prg.write(bytearray(bytesArr[sameBytes[prgCounter]]))
            bytesWritten += 1
            if prgCounter + 1 < len(sameBytes):
                prgCounter += 1
            else:
                finish = True
        else:
            byteString = random.choices(bytesArr, k = 1)
            bytesWritten += 1
            prg.write(bytearray(byteString))
            prgCounter += 1

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    romCRC32 = str(crc32("file" + str(i + 1) + ".bin"))
    romMD5 = str(md5_GEN("file" + str(i + 1) + ".bin"))
    romSHA1 = str(sha1_GEN("file" + str(i + 1) + ".bin"))
    romSHA256 = str(sha256_GEN("file" + str(i + 1) + ".bin"))

    prg.close()

    if i == 0:
        if os.path.getsize("file1.bin") == numStop:
            input(bytesWritten)
        else:
            print(bytesWritten)
            print(str(os.path.getsize("file1.bin")))
            raise Exception("Script is not working properly!")

    for games in range(len(gameName)):
        if romCRC32 == crc_LSS[games].replace(" ", "") and romMD5 == md5_LSS[games].replace(" ", "") and romSHA1 == sha1_LSS[games].replace(" ", "") and romSHA256 == sha256_LSS[games].replace(" ", ""):
            satisfied = True
            print("This file has the correct ROM and file hashes!")
            print("You have successfully built a copy of " + gameName[games] + "! Add an INES header to this to get this working.")
            break
        else:
            print("File" + str(i + 1) + ".bin has the wrong file hashes. Retrying...")
            if system == "windows" and games == len(gameName):
                os.system("del file" + str(i + 1) + ".bin")
            elif system == "linux" and games == len(gameName):
                os.system("rm file" + str(i + 1) + ".bin")

    print("You have built " + str(i + 1) + " files.")
    i += 1
