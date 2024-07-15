# Thanks to @ranman for the response at https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
# And @CrouZ for the response at https://stackoverflow.com/questions/1742866/compute-crc-of-file-in-python

import random
import os.path
import os
import hashlib
import zlib
import sys
sys.set_int_max_str_digits(0)
satisfied = False
i = 0

question = input("Would you like to delete corrupt files? ")
numOfGames = int(input("How many games would you like to compare these hashes to? "))
registeredGames = 0
gameName = []

if numOfGames == 0:
    raise Exception("Why are you running this program then??")

while registeredGames < numOfGames:
    gameName.append(input("Game: "))
    registeredGames += 1

crc_LSS = []
md5_LSS = []
sha1_LSS = []
sha256_LSS = []
crc_HDR = []
md5_HDR = []
sha1_HDR = []
sha256_HDR = []

print("Only compare ROMs with the same header. Otherwise, there will be garbage data in the header and the hashes will not match.")

for games in gameName:
    crc_LSS.append(input("CRC of ROM (unheadered): "))
    md5_LSS.append(input("MD5 of ROM (unheadered): "))
    sha1_LSS.append(input("SHA1 of ROM (unheadered): "))
    sha256_LSS.append(input("SHA256 of ROM (unheadered): "))
    crc_HDR.append(input("CRC of File (headered): "))
    md5_HDR.append(input("MD5 of File (headered): "))
    sha1_HDR.append(input("SHA1 of File (headered): "))
    sha256_HDR.append(input("SHA256 of File (headered): "))


print("Use a hex to decimal converter to get the decimal equivalent-numbers from the 16-byte headers. They will be converted back into hex numbers.")
headerByte_00 = int(input("Byte 1: "))
headerByte_01 = int(input("Byte 2: "))
headerByte_02 = int(input("Byte 3: "))
headerByte_03 = int(input("Byte 4: "))
headerByte_04 = int(input("Byte 5: "))
headerByte_05 = int(input("Byte 6: "))
headerByte_06 = int(input("Byte 7: "))
headerByte_07 = int(input("Byte 8: "))
headerByte_08 = int(input("Byte 9: "))
headerByte_09 = int(input("Byte 10: "))
headerByte_0A = int(input("Byte 11: "))
headerByte_0B = int(input("Byte 12: "))
headerByte_0C = int(input("Byte 13: "))
headerByte_0D = int(input("Byte 14: "))
headerByte_0E = int(input("Byte 15: "))
headerByte_0F = int(input("Byte 16: "))
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
numStop = int(input("How large is the .nes file with the header? "))

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

if numStop != 24592 and numStop != 40976:
    raise Exception("The ROM size can only be 24,592 bytes or 40,976 bytes!")

def optimize(val, power):
    result = pow(val, power//2)
    result = result * result
 
    if power % 2 != 0:
        result = result * val
    return result
 
 
possibilities = optimize(256, numStop - 16)
input("You are attempting to add " + str(possibilities) + " files. Are you sure about this? ")

while satisfied == False and i < possibilities:
    while os.path.isfile("file" + str(i + 1) + ".nes"):
        if question == "no":
            i += 1
        elif question == "yes":
            os.system("del *.nes")
            os.system("del *.bin")

    file = open("file" + str(i + 1) + ".nes", "wb")
    prg = open("file" + str(i + 1) + ".bin", "wb")
    header = open("header.bin", "wb")

    bytesArr = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF]
    bytesWritten = 0

    while bytesWritten < numStop:
        byteString = random.choices(bytesArr, k = numStop - 16)
        if bytesWritten < 16:
            header.write(bytearray([bytesArr[headerByte_00], bytesArr[headerByte_01], bytesArr[headerByte_02], bytesArr[headerByte_03], bytesArr[headerByte_04], bytesArr[headerByte_05], bytesArr[headerByte_06], bytesArr[headerByte_07], bytesArr[headerByte_08], bytesArr[headerByte_09], bytesArr[headerByte_0A], bytesArr[headerByte_0B], bytesArr[headerByte_0C], bytesArr[headerByte_0D], bytesArr[headerByte_0E], bytesArr[headerByte_0F]]))
            bytesWritten += 16
            file.write(bytearray([bytesArr[headerByte_00], bytesArr[headerByte_01], bytesArr[headerByte_02], bytesArr[headerByte_03], bytesArr[headerByte_04], bytesArr[headerByte_05], bytesArr[headerByte_06], bytesArr[headerByte_07], bytesArr[headerByte_08], bytesArr[headerByte_09], bytesArr[headerByte_0A], bytesArr[headerByte_0B], bytesArr[headerByte_0C], bytesArr[headerByte_0D], bytesArr[headerByte_0E], bytesArr[headerByte_0F]]))
        else:
            file.write(bytearray(byteString))
            prg.write(bytearray(byteString))
            bytesWritten += numStop - 16
    
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    fileCRC32 = str(crc32("file" + str(i + 1) + ".nes"))
    fileMD5 = str(md5_GEN("file" + str(i + 1) + ".nes"))
    fileSHA1 = str(sha1_GEN("file" + str(i + 1) + ".nes"))
    fileSHA256 = str(sha256_GEN("file" + str(i + 1) + ".nes"))

    romCRC32 = str(crc32("file" + str(i + 1) + ".bin"))
    romMD5 = str(md5_GEN("file" + str(i + 1) + ".bin"))
    romSHA1 = str(sha1_GEN("file" + str(i + 1) + ".bin"))
    romSHA256 = str(sha256_GEN("file" + str(i + 1) + ".bin"))


    for games in range(len(gameName)):
        if romCRC32 == crc_LSS[games].replace(" ", "") and romMD5 == md5_LSS[games].replace(" ", "") and romSHA1 == sha1_LSS[games].replace(" ", "") and romSHA256 == sha256_LSS[games].replace(" ", ""):
            satisfied = True
            if fileCRC32 == crc_HDR[games].replace(" ", "") and fileMD5 == md5_HDR[games].replace(" ", "") and fileSHA1 == sha1_HDR[games].replace(" ", "") and fileSHA256 == sha256_HDR[games].replace(" ", ""):
                print("This file has the correct ROM and file hashes!")
                print("You have successfully built a copy of " + gameName[games] + "!")
            else:
                print("File" + str(i + 1) + ".nes has the correct ROM hashes but the wrong file hashes. The header may be the problem.")
        elif fileCRC32 == crc_HDR[games].replace(" ", "") and fileMD5 == md5_HDR[games].replace(" ", "") and fileSHA1 == sha1_HDR[games].replace(" ", "") and fileSHA256 == sha256_HDR[games].replace(" ", ""):
            satisfied = True
            if romCRC32 == crc_LSS[games].replace(" ", "") and romMD5 == md5_LSS[games].replace(" ", "") and romSHA1 == sha1_LSS[games].replace(" ", "") and romSHA256 == sha256_LSS[games].replace(" ", ""):
                print("This file has the correct ROM and file hashes!")
                print("You have successfully built a copy of " + gameName[games] + "!")
            else:
                print("File" + str(i + 1) + ".nes has the correct file hashes but the wrong rom hashes. The ROM has a high chance of crashing, so it is suggested you retry this script.")
        else:
            print("File" + str(i + 1) + ".nes has the wrong file hashes and the wrong ROM hashes. Retrying...")
            if question == "yes" and i > 0:
                os.system("del file" + str(i + 1) + ".nes")
                os.system("del file" + str(i + 1) + ".bin")
            elif question == "no" or question == "yes" and i == 0:
                print("Moving to the next file.")
            else:
                raise Exception("Your answer to \"Would you like to delete corrupt files?\" can only be [yes] or [no]!")

    print("You have built " + str(i + 1) + " files.")
    i += 1
    if i >= 122022 / 2 and numStop == 40976 or i >= 203318 / 2 and numStop == 24592:
        if question == "no" and i%(122022 / 2) == 0 and numStop == 40976 or question == "no" and i%(203318 / 2) == 0 and numStop == 24592:
            os.system("git config --global user.name " + input("git config --global user.name: "))
            os.system("git config --global user.email " + input("git config --global user.email: "))
            gitHost = "git clone " + input("git clone: ")
            os.system(gitHost)
            print("Paste the name of the git repository you just cloned. Otherwise, the script will not work properly.")
            gitRepo = input("Name of Git Repository: ")
            os.system("move *.bin " + gitRepo)
            os.system("move *.nes " + gitRepo)
            os.system("cd " + gitRepo)
            os.system("move header.bin ..")
            os.system("git switch --create master")
            os.system("git init --initial-branch=master")
            os.system("git remote add origin " + gitHost.replace("git clone ", ""))
            os.system("git add .")
            os.system("git commit -m \"Update files\"")
            os.system("git push --set-upstream origin master")
            os.system("cd ..")
            os.system("del " + gitRepo)
