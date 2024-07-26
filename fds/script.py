import random
import sys
import os 
import hashlib
import zlib
sys.set_int_max_str_digits(0)
satisfied = False
i = 0
sameBytes = []
bytesLoc = []
bytesArr = [B'\x00', B'\x01', B'\x02', B'\x03', B'\x04', B'\x05', B'\x06', B'\x07', B'\x08', B'\x09', B'\x0A', B'\x0B', B'\x0C', B'\x0D', B'\x0E', B'\x0F', B'\x10', B'\x11', B'\x12', B'\x13', B'\x14', B'\x15', B'\x16', B'\x17', B'\x18', B'\x19', B'\x1A', B'\x1B', B'\x1C', B'\x1D', B'\x1E', B'\x1F', B'\x20', B'\x21', B'\x22', B'\x23', B'\x24', B'\x25', B'\x26', B'\x27', B'\x28', B'\x29', B'\x2A', B'\x2B', B'\x2C', B'\x2D', B'\x2E', B'\x2F', B'\x30', B'\x31', B'\x32', B'\x33', B'\x34', B'\x35', B'\x36', B'\x37', B'\x38', B'\x39', B'\x3A', B'\x3B', B'\x3C', B'\x3D', B'\x3E', B'\x3F', B'\x40', B'\x41', B'\x42', B'\x43', B'\x44', B'\x45', B'\x46', B'\x47', B'\x48', B'\x49', B'\x4A', B'\x4B', B'\x4C', B'\x4D', B'\x4E', B'\x4F', B'\x50', B'\x51', B'\x52', B'\x53', B'\x54', B'\x55', B'\x56', B'\x57', B'\x58', B'\x59', B'\x5A', B'\x5B', B'\x5C', B'\x5D', B'\x5E', B'\x5F', B'\x60', B'\x61', B'\x62', B'\x63', B'\x64', B'\x65', B'\x66', B'\x67', B'\x68', B'\x69', B'\x6A', B'\x6B', B'\x6C', B'\x6D', B'\x6E', B'\x6F', B'\x70', B'\x71', B'\x72', B'\x73', B'\x74', B'\x75', B'\x76', B'\x77', B'\x78', B'\x79', B'\x7A', B'\x7B', B'\x7C', B'\x7D', B'\x7E', B'\x7F', B'\x80', B'\x81', B'\x82', B'\x83', B'\x84', B'\x85', B'\x86', B'\x87', B'\x88', B'\x89', B'\x8A', B'\x8B', B'\x8C', B'\x8D', B'\x8E', B'\x8F', B'\x90', B'\x91', B'\x92', B'\x93', B'\x94', B'\x95', B'\x96', B'\x97', B'\x98', B'\x99', B'\x9A', B'\x9B', B'\x9C', B'\x9D', B'\x9E', B'\x9F', B'\xA0', B'\xA1', B'\xA2', B'\xA3', B'\xA4', B'\xA5', B'\xA6', B'\xA7', B'\xA8', B'\xA9', B'\xAA', B'\xAB', B'\xAC', B'\xAD', B'\xAE', B'\xAF', B'\xB0', B'\xB1', B'\xB2', B'\xB3', B'\xB4', B'\xB5', B'\xB6', B'\xB7', B'\xB8', B'\xB9', B'\xBA', B'\xBB', B'\xBC', B'\xBD', B'\xBE', B'\xBF', B'\xC0', B'\xC1', B'\xC2', B'\xC3', B'\xC4', B'\xC5', B'\xC6', B'\xC7', B'\xC8', B'\xC9', B'\xCA', B'\xCB', B'\xCC', B'\xCD', B'\xCE', B'\xCF', B'\xD0', B'\xD1', B'\xD2', B'\xD3', B'\xD4', B'\xD5', B'\xD6', B'\xD7', B'\xD8', B'\xD9', B'\xDA', B'\xDB', B'\xDC', B'\xDD', B'\xDE', B'\xDF', B'\xE0', B'\xE1', B'\xE2', B'\xE3', B'\xE4', B'\xE5', B'\xE6', B'\xE7', B'\xE8', B'\xE9', B'\xEA', B'\xEB', B'\xEC', B'\xED', B'\xEE', B'\xEF', B'\xF0', B'\xF1', B'\xF2', B'\xF3', B'\xF4', B'\xF5', B'\xF6', B'\xF7', B'\xF8', B'\xF9', B'\xFA', B'\xFB', B'\xFC', B'\xFD', B'\xFE', B'\xFF']

if os.path.isfile('bytes.dat') and os.path.isfile('byteloc.dat'):
    with open('bytes.dat') as f:
        lines = [line.rstrip() for line in f]
        for bytes in range(len(lines)):
            if lines[bytes].isspace() == False:
                sameBytes.append(bytesArr[int(lines[bytes])])
        f.close()

    with open('byteloc.dat') as f:
        loc = [loc.rstrip() for loc in f]
        for bytes in range(len(loc)):
            if loc[bytes].isspace() == False:
                bytesLoc.append(int(loc[bytes]))
        f.close()
else:
    raise Exception("Run script2.py before running this script!")

gameName = []
crc_LSS = []
md5_LSS = []
sha1_LSS = []

mode = 0

if os.path.isfile('fds.dat'):
    with open('fds.dat') as f:
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
                mode = 0
        f.close()
else:
    raise Exception("FDS.dat does not exist!")

numStop = int(input("How large is the .fds file? "))
while os.path.isfile("file" + str(i + 1) + ".fds"):
    i += 1
    os.remove("file" + str(i) + ".fds")
    
i = 0
while satisfied == False:
    if i > 0:
        os.remove("file" + str(i) + ".fds")

    prg = open("file" + str(i + 1) + ".fds", "wb")

    bytesWritten = 0
    prgCounter = 0
    finish = False

    while bytesWritten < numStop:
        if len(sameBytes) > 0 and bytesWritten == bytesLoc[prgCounter] and finish == False:
            byteString = sameBytes[prgCounter]
            prg.write(byteString)
            bytesWritten += 1
            if prgCounter < len(sameBytes):
                prgCounter += 1
            else:
                finish = True
        else:
            bytesArr = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF]
            byteString = random.choices(bytesArr, k = 1)
            prg.write(bytearray(byteString))
            bytesWritten += 1
            if prgCounter < len(sameBytes):
                prgCounter += 1
            else:
                finish = True

    prg.close()

    prg = open("file" + str(i + 1) + ".fds", "rb")
    prgRead = prg.read()

    romCRC32 = zlib.crc32(prgRead)
    romCRC32 = str(hex(romCRC32))
    romCRC32 = romCRC32.replace("0x", "")
    romMD5 = str(hashlib.md5(prgRead).hexdigest())
    romSHA1 = str(hashlib.sha1(prgRead).hexdigest())

    prg.close()

    for games in range(len(gameName)):
        if romCRC32 == crc_LSS[games] or romMD5 == md5_LSS[games] or romSHA1 == sha1_LSS[games]:
            satisfied = True
            print("This file has the correct ROM and file hashes!")
            print("You have successfully built a copy of " + gameName[games] + "!")
            break
    print("File" + str(i + 1) + ".fds has the wrong file hashes. Retrying...")
    i += 1
