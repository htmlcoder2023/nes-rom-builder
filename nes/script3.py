datFile = open("nes.dat", "r")
linesArr = []
crc32 = []
md5 = []
sha1 = []
sha256 = []
specifiedInput = input("What instances do you want to find? For example, the instance size=\"40960\" can be used to find all ROMs with a size of 40 kilobytes. ")

while True:
    line = datFile.readline()
    if specifiedInput in line:
        line = line.replace("		", "")
        line = line.replace('<rom name="', "")
        line = line.split('"')
        print(line[0])
        if "nodump" not in line[2]:
            print(line[4])
            print(line[6])
            print(line[8])
            print(line[10])
        linesArr.append(str(line[0]))
        if "nodump" not in line[2]:   
            linesArr.append(str(line[4]))
            linesArr.append(str(line[6]))
            linesArr.append(str(line[8]))
            linesArr.append(str(line[10]))
            print(str(int(len(linesArr) / 5)) + " games added.")
        else:
            print(str(int(len(linesArr))) + " games added.")
    if not line:
        break

datFile.close()

datFile = open("nes.dat", "w")

lines = 0

while lines < len(linesArr):
    if lines == 0:
        datFile.write(linesArr[lines])
    else:
        datFile.write("\n" + linesArr[lines])
    lines += 1

datFile.close()