datFile = open("nes.dat", "r")
linesArr = []
crc32 = []
md5 = []
sha1 = []
sha256 = []
specifiedInput = input("What instances do you want to find? For example, the instance size=\"40960\" can be used to find all ROMs with a size of 40 kilobytes. ")
mode = input("Game Check? ")
if mode == "yes":
    setPublisher = input("What publisher are you targeting? ")

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
    if not line:
        break

datFile.close()

datFile = open("nes.dat", "w")

lines = 0

print("There are " + str(int(len(linesArr) / 5)) + " matches for your input!")

while lines < len(linesArr):
    if lines == 0:
        datFile.write(linesArr[lines])
    else:
        datFile.write("\n" + linesArr[lines])
    lines += 1

counter = 0
counterCMP = len(linesArr)

if mode == "yes":
    while counter < counterCMP:
        print(linesArr[counter])
        game = input("Game: ")
        publisher = input("Publisher: ")
        if game == "" or publisher == "":
            break
        if game in linesArr[counter] and publisher != setPublisher:
            linesArr.pop(counter)
            counterCMP -= 1
        elif game in linesArr[counter] and publisher == setPublisher:
            counter += 1
        else:
            raise Exception("Game not found!")
    open("nes.dat", "w")
    lines = 0
    print("There are " + str(len(linesArr)) + " matches for your input!")
    while lines < len(linesArr):
        if lines == 0:
            datFile.write(linesArr[lines])
        else:
            datFile.write("\n" + linesArr[lines])
        lines += 1
elif mode == "no":
    print("Program execution complete.")
else:
    raise Exception("The answer to [Game Check?] can only be [yes] or [no]!")

datFile.close()
