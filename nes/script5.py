import os
import hashlib
import zlib
datFile = open("nes.dat", "r")
lines = []
while True:
    line = datFile.readline()
    if '<rom name="' and 'size="' in line:
        line = line.replace("		", "")
        line = line.replace('<rom name="', "")
        line = line.split('"')
        print(line[0])
        print(line[2])
        print(line[4])
        print(line[6])
        print(line[8])
        print(line[10])
        lines.append(line[0])
        lines.append(line[2])
        lines.append(line[4])
        lines.append(line[6])
        lines.append(line[8])
        lines.append(line[10])
    if not line:
        break
datFile.close()