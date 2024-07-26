import os
import hashlib
import zlib
datFile = open("nes.dat", "r")
lines = []
linesArr = []
sizes = []
fileWrite = []
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
        os.system("mkdir " + line[2])
        linesArr.append(line[2])
        sizes.append(open(line[2] + "/nes.dat", "w"))
        fileWrite.append(0)
    if not line:
        break

while True:
    line = datFile.readline()
    if '<rom name="' and 'size="' in line:
        line = line.replace("		", "")
        line = line.replace('<rom name="', "")
        line = line.split('"')
        for arrs in range(len(sizes)):
            if line[2] == linesArr[arrs]:
                if fileWrite[arrs] == 0:
                    sizes[arrs].write(lines[0])
                    sizes[arrs].write(lines[2])
                    sizes[arrs].write(lines[4])
                    sizes[arrs].write(lines[6])
                    sizes[arrs].write(lines[8])
                    sizes[arrs].write(lines[10])
                else:
                    sizes[arrs].write("\n" + lines[0])
                    sizes[arrs].write("\n" + lines[2])
                    sizes[arrs].write("\n" + lines[4])
                    sizes[arrs].write("\n" + lines[6])
                    sizes[arrs].write("\n" + lines[8])
                    sizes[arrs].write("\n" + lines[10])
                fileWrite[arrs] += 1
    if not line:
        break

datFile.close()