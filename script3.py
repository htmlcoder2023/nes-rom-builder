datFile = open("nes.dat", "r")
linesArr = []
specifiedInput = input("What instances do you want to find? For example, the instance size=\"40960\" can be used to find all ROMs with a size of 40 kilobytes. ")
mode = input("Game Check? ")
if mode == "yes":
    setPublisher = input("What publisher are you targeting? ")

while True:
    line = datFile.readline()
    if specifiedInput in line:
        linesArr.append(line)
    if not line:
        break

datFile.close()

datFile = open("nes.dat", "w")

lines = 0

print("There are " + str(len(linesArr)) + " matches for your input!")

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
        game = input("Game: ")
        publisher = input("Publisher: ")
        for games in range(len(linesArr)):
            if game in linesArr[games] and publisher != setPublisher:
                linesArr.pop(games)
            else:
                break
        counter += 1
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