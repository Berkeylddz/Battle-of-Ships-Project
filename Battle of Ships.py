"""Berke Abdullah Yıldız 2210356100"""
import sys
outputFile = open("Battleship.out","w")
try:
    try:
        player1Datas = open(sys.argv[1],"r")
    except IOError:
        print("IOError: input file " + sys.argv[1] + " is not reachable.")
        outputFile.write("IOError: input file " + sys.argv[1] + " is not reachable.")
        exit()

    try:
        player2Datas = open(sys.argv[2])
    except IOError:
        print("IOError: input file " + sys.argv[2]+ " is not reachable.")
        outputFile.write("IOError: input file " + sys.argv[2]+ " is not reachable.")
        exit()

    try:
        player2Moves = open(sys.argv[4])
    except IOError:
        print("IOError: input file " + sys.argv[4]+ " is not reachable.")
        outputFile.write("IOError: input file " + sys.argv[4]+ " is not reachable.")
        exit()

    try:
        player1Moves = open(sys.argv[3])
    except IOError:
        print("IOError: input file " + sys.argv[3]+ " is not reachable.")
        outputFile.write("IOError: input file " + sys.argv[3]+ " is not reachable.")
        exit()

except IndexError:
    print("IndexError: list index out of range")
    outputFile.write("IndexError: list index out of range")
    exit()

player1Infos = open(sys.argv[1]).readlines()
player1List = []

player2Infos = open(sys.argv[2]).readlines()
player2List = []

for i in range(len(player1Infos)):
    takePlayer1Infos = player1Datas.readline().rstrip("\n").split(";")
    player1List.append(takePlayer1Infos)

for i in range(len(player1Infos)):
    takePlayer2Infos = player2Datas.readline().rstrip("\n").split(";")
    player2List.append(takePlayer2Infos)

player1MovesNumber = open(sys.argv[3]).readlines()
player2MovesNumber = open(sys.argv[4]).readlines()

takePlayer1Moves = player1Moves.readline().split(";")
takePlayer2Moves = player2Moves.readline().split(";")

round = 1

player1oyunHareket = []
player11 = []
for a in range(10):
    player11 = []
    for x in range(10):
        player11.append("-")
    player1oyunHareket.append(player11)

player2oyunHareket = []
player22 = []
for a in range(10):
    player22 = []
    for x in range(10):
        player22.append("-")
    player2oyunHareket.append(player22)

print("Battle of Ships Game\n")
outputFile.write("Battle of Ships Game")
outputFile.write("\n")
harfler = "ABCDEFGHIJ"

def playerShips(ship,shipInfo,dict):
    """The only purpose of this function is not to repeat the same things as the function I used to find ships."""
    harfler = "ABCDEFGHIJ"
    ship = shipInfo.readlines()
    for i in range(len(ship)):
        isim = ship[i][0:2]
        satır = ship[i].split(":")[1].split(",")[0]
        sütun = ship[i].split(":")[1].split(",")[1][0]
        taraf = ship[i].split(";")[1]
        sütunHarfi = harfler.index(sütun)
        numberDict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        if isim[0] == "B":
            if taraf == "right":
                dict[isim] = [harfler[sütunHarfi] + satır, harfler[sütunHarfi + 1] + satır,
                                    harfler[sütunHarfi + 2] + satır, harfler[sütunHarfi + 3] + satır]
            elif taraf == "down":
                dict[isim] = [sütun + satır, sütun + str(int(satır) + 1), sütun + str(int(satır) + 2),
                                    sütun + str(int(satır) + 3)]
        elif isim[0] == "P":
            if taraf == "right":
                dict[isim] = [harfler[sütunHarfi] + satır, harfler[sütunHarfi + 1] + satır]

            elif taraf == "down":
                dict[isim] = [sütun + satır, sütun + str(int(satır) + 1)]

def player1Ships():
    """this function is to find ships."""
    global ships1Dict,player1Ships,player1ShipsInfos
    for i in range(10):
        if "C" in player1List[i]:
            indexOfC = player1List[i].index("C")
            if player1List[i][indexOfC + 1] == "C":
                ships1Dict["C"] = [harfler[indexOfC] + str(i + 1), harfler[indexOfC + 1] + str(i + 1),
                                   harfler[indexOfC + 2]
                                   + str(i + 1), harfler[indexOfC + 3] + str(i + 1), harfler[indexOfC + 4] + str(i + 1)]
            else:
                ships1Dict["C"].append(harfler[indexOfC] + str(i + 1))

        if "S" in player1List[i]:
            indexOfS = player1List[i].index("S")
            if player1List[i + 1][indexOfS] == "S":
                ships1Dict["S"].append(harfler[indexOfS] + str(i + 1))

            else:
                ships1Dict["S"] = [harfler[indexOfS] + str(i + 1), harfler[indexOfS + 1] + str(i + 1),
                                   harfler[indexOfS + 2] + str(i + 1)]

        if "D" in player1List[i]:
            indexOfD = player1List[i].index("D")
            try:
                if player1List[i + 1][indexOfD] == "D":
                    ships1Dict["D"] = [harfler[indexOfD] + str(i), harfler[indexOfD] + str(i + 1),
                                       harfler[indexOfD] + str(i + 2)]
            except:
                pass
            try:
                if player1List[i][indexOfD + 1] == "D":
                    ships1Dict["D"] = [harfler[indexOfD] + str(i + 1), harfler[indexOfD + 1] + str(i + 1),
                                       harfler[indexOfD + 2] + str(i + 1)]
            except:
                pass
ships1Dict = {"B1": [], "B2": [], "P1": [], "P2": [], "P3": [], "P4": [], "C": [], "S": [], "D": []}
player1ShipsInfos = open("OptionalPlayer1.txt", "r")
playerShips(player1Ships,player1ShipsInfos,ships1Dict)

def player2Ships():
    """this function is to find ships."""
    global ships2Dict
    harfler = "ABCDEFGHIJ"
    player2Ships = player2ShipsInfos.readlines()
    for i in range(10):
        if "C" in player2List[i]:
            indexOfC = player2List[i].index("C")
            if player2List[i][indexOfC + 1] == "C":
                ships2Dict["C"] = [harfler[indexOfC] + str(i + 1), harfler[indexOfC + 1] + str(i + 1),
                                   harfler[indexOfC + 2]
                                   + str(i + 1), harfler[indexOfC + 3] + str(i + 1), harfler[indexOfC + 4] + str(i + 1)]
            else:
                ships2Dict["C"].append(harfler[indexOfC] + str(i + 1))

        if "S" in player2List[i]:
            indexOfS = player2List[i].index("S")
            if player2List[i][indexOfS] == "S":
                ships2Dict["S"].append(harfler[indexOfS] + str(i + 1))

            else:
                ships2Dict["S"] = [harfler[indexOfC] + str(i + 1), harfler[indexOfC + 1] + str(i + 1),
                                   harfler[indexOfC + 2] + str(i + 1)]

        if "D" in player2List[i]:
            indexOfD = player2List[i].index("D")
            try:
                if player2List[i + 1][indexOfD] == "D":
                    ships2Dict["D"] = [harfler[indexOfD] + str(i), harfler[indexOfD] + str(i + 1),
                                       harfler[indexOfD] + str(i + 2)]

            except:
                ships2Dict["D"].append(harfler[indexOfD] + str(i + 1))

player2ShipsInfos = open("OptionalPlayer2.txt", "r")
ships2Dict = {"B1": [], "B2": [], "P1": [], "P2": [], "P3": [], "P4": [], "C": [], "S": [], "D": []}
playerShips(player2Ships, player2ShipsInfos, ships2Dict)

player1Ships()
player2Ships()

player1ShipsPosition = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-","P4": "-"}
player2ShipsPosition = {"C": "-", "B1": "-", "B2": "-", "D": "-", "S": "-", "P1": "-", "P2": "-", "P3": "-","P4": "-"}

player1PatrolBoat = {"P1": "-", "P2": "-", "P3": "-","P4": "-"}
player2PatrolBoat = {"P1": "-", "P2": "-", "P3": "-","P4": "-"}
patrolBoat1=["-","-","-","-"]
patrolBoat2=["-","-","-","-"]
def shipsApperance(dict,position,patrol):
    """this function checks sinking ships and checks sinking chart"""
    if dict["B1"][0] == "-" and dict["B1"][1] == "-" and dict["B1"][2] == "-" and dict["B1"][
        3] == "-":
        position["B1"] = "X "

    if dict["B2"][0] == "-" and dict["B2"][1] == "-" and dict["B2"][2] == "-" and dict["B2"][
        3] == "-":
        position["B2"] = "X "

    if dict["C"][0] == "-" and dict["C"][1] == "-" and dict["C"][2] == "-" and dict["C"][
        3] == "-" and ships2Dict["C"][4] == "-":
        position["C"] = "X "

    if dict["D"][0] == "-" and dict["D"][1] == "-" and dict["D"][2] == "-":
        position["D"] = "X"

    if dict["S"][0] == "-" and dict["S"][1] == "-" and dict["S"][2] == "-":
        position["S"] = "X"

    if dict["P1"][0] == "-" and dict["P1"][1] == "-":
        patrol["P3"] = "X"

        position["P1"] = "X"
        patrol["P1"] = "X"

    if dict["P2"][0] == "-" and dict["P2"][1] == "-":
        position["P2"] = "X"
        patrol["P2"] = "X"

    if dict["P3"][0] == "-" and dict["P3"][1] == "-":
        position["P3"] = "X"
    if dict["P4"][0] == "-" and dict["P4"][1] == "-":
        position["P4"] = "X"
        patrol["P4"] = "X"

def printShipsName():
    """this function is for printing the status of ships"""
    number1=0
    number2 = 0
    ships= ["P1","P2","P3","P4"]
    for i in range(len(player1PatrolBoat)):
        if player1PatrolBoat[ships[i]] == "X":
            number1+=1
    for i in range(number1):
        patrolBoat1[i]= "X"

    for i in range(len(player2PatrolBoat)):
        if player2PatrolBoat[ships[i]] == "X":
            number2+=1
    for i in range(number2):
        patrolBoat2[i]= "X"

    print("\nCarrier\t      " + "%s\t\t\tCarrier       %s" % (player1ShipsPosition["C"], player2ShipsPosition["C"]))
    print("Battleship    " + "%s%s\t\t\t" % (player1ShipsPosition["B1"], player1ShipsPosition["B2"]) + "Battleship    %s %s" % (player2ShipsPosition["B1"], player2ShipsPosition["B2"]))
    print("Destroyer     " + "%s\t\t\t" % player1ShipsPosition["D"] + "        Destroyer     %s" % player2ShipsPosition["D"])
    print("Submarine     " + "%s\t\t\t" % player1ShipsPosition["S"] + "        Submarine     %s" % player2ShipsPosition["S"])
    print("Patrol Boat   " + "%s %s %s %s\t\t" % (patrolBoat1[0],patrolBoat1[1],patrolBoat1[2],patrolBoat1[3]) + "        Patrol Boat   %s %s %s %s" %
          (patrolBoat2[0],patrolBoat2[1],patrolBoat2[2],patrolBoat2[3]))

    outputFile.write("\nCarrier\t\t" + "%s\t\t\t\tCarrier\t\t%s" % (player1ShipsPosition["C"], player2ShipsPosition["C"]))
    outputFile.write("\nBattleship" + "\t%s%s\t\t\t\t" % (player1ShipsPosition["B1"], player1ShipsPosition["B2"]) + "Battleship\t%s %s" % (player2ShipsPosition["B1"], player2ShipsPosition["B2"]))
    outputFile.write(("\nDestroyer\t" + "%s\t\t\t\t" % player1ShipsPosition["D"] + "Destroyer\t%s" % player2ShipsPosition["D"]))
    outputFile.write(("\nSubmarine\t" + "%s\t\t\t\t" % player1ShipsPosition["S"] + "Submarine\t%s" % player2ShipsPosition["S"]))
    outputFile.write("\nPatrol Boat\t" + "%s %s %s %s\t\t\t" % (patrolBoat1[0],patrolBoat1[1],patrolBoat1[2],patrolBoat1[3]) + "Patrol Boat\t%s %s %s %s" %
                     (patrolBoat2[0],patrolBoat2[1],patrolBoat2[2],patrolBoat2[3]))

def makeTable():
    """this function is the table where I show the ships hit"""
    for row in range(10):
        if row == 9:
            print(str(row + 1), end="")
            outputFile.write(str(row + 1))
        else:
            print(str(row + 1), end=" ")
            outputFile.write(str(row + 1)+" ")
        for col in range(10):
            print(player1oyunHareket[row][col], end=" ")
            outputFile.write(player1oyunHareket[row][col]+" ")
        print("\t\t\t", end="")
        outputFile.write("\t\t")

        if row == 9:
            print(str(row + 1), end="")
            outputFile.write(str(row + 1))
        else:
            print(str(row + 1), end=" ")
            outputFile.write(str(row + 1)+" ")

        for col in range(10):
            print(player2oyunHareket[row][col], end=" ")
            outputFile.write(player2oyunHareket[row][col]+" ")
        print()
        outputFile.write("\n")

def player1Move(index):
    """this function makes the move of player 1"""
    global round, sungedShip2Number, player2ShipsPosition, player1ShipsPosition, shipNameList
    print("Player1’s Move\n")
    print("Round : " + str(round) + "\t\t\t\tGrid Size: 10x10\n")
    print("Player1’s Hidden Board\t\t\tPlayer2’s Hidden Board")
    print("  A B C D E F G H I J\t\t\t  A B C D E F G H I J")

    outputFile.write("\nPlayer1’s Move\n")
    outputFile.write("\nRound : " + str(round) + "\t\t\t\t\tGrid Size: 10x10\n")
    outputFile.write("\nPlayer1’s Hidden Board\t\tPlayer2’s Hidden Board\n")
    outputFile.write("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")

    sayı = takePlayer1Moves[index].split(",")[0]
    harf = takePlayer1Moves[index].split(",")[1]

    makeTable()
    shipsApperance(ships1Dict, player1ShipsPosition, player1PatrolBoat)
    shipsApperance(ships2Dict, player2ShipsPosition, player2PatrolBoat)
    printShipsName()

    print("\nEnter your move: " + str(sayı) + "," + harf)
    print()
    outputFile.write("\n\nEnter your move: " + str(sayı) + "," + harf+"\n")

    if player2List[int(sayı) - 1][harfler.index(harf)] == "":
        player2oyunHareket[int(sayı) - 1][harfler.index(harf)] = "O"
        player2List[int(sayı) - 1][harfler.index(harf)] = "O"
    else:
        player2oyunHareket[int(sayı) - 1][harfler.index(harf)] = "X"
        player2List[int(sayı) - 1][harfler.index(harf)] = "X"

    konum = harf + sayı

    shipNameList = ["B1", "B2", "P1", "P2", "P3", "P4", "C", "S", "D"]
    for i in range(len(ships2Dict)):
        try:
            shipName = ships2Dict[shipNameList[i]].index(konum)
        except:
            pass

        if konum in ships2Dict[shipNameList[i]]:
            ships2Dict[shipNameList[i]][shipName] = "-"

def player2Move(index):
    """this function makes the move of player 2"""
    global round, sungedShip1Number, player1ShipsPosition, player2ShipsPosition, shipNameList
    print("Player2’s Move\n")
    print("Round : " + str(round) + "\t\t\t\tGrid Size: 10x10\n")
    print("Player1’s Hidden Board\t\t\tPlayer2’s Hidden Board")
    print("  A B C D E F G H I J\t\t\t  A B C D E F G H I J")
    outputFile.write("\nPlayer2’s Move\n")
    outputFile.write("\nRound : " + str(round) + "\t\t\t\t\tGrid Size: 10x10\n")
    outputFile.write("\nPlayer1’s Hidden Board\t\tPlayer2’s Hidden Board\n")
    outputFile.write("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")

    sayı = int(takePlayer2Moves[index].split(",")[0])
    harf = takePlayer2Moves[index].split(",")[1]
    makeTable()
    shipsApperance(ships1Dict, player1ShipsPosition, player1PatrolBoat)
    shipsApperance(ships2Dict, player2ShipsPosition, player2PatrolBoat)
    printShipsName()
    print("\nEnter your move: " + str(sayı) + "," + harf)
    print()
    outputFile.write("\n\nEnter your move: " + str(sayı) + "," + harf+"\n")

    if player1List[sayı - 1][harfler.index(harf)] == "":
        player1oyunHareket[sayı - 1][harfler.index(harf)] = "O"
        player1List[sayı-1][harfler.index(harf)] = "O"
    else:
        player1oyunHareket[sayı - 1][harfler.index(harf)] = "X"
        player1List[sayı - 1][harfler.index(harf)] = "X"

    round += 1
    konum = harf + str(sayı)
    shipNameList = ["B1", "B2", "P1", "P2", "P3", "P4", "C", "S", "D"]
    for i in range(len(ships1Dict)):
        try:
            shipName = ships1Dict[shipNameList[i]].index(konum)
        except:
            pass

        if konum in ships1Dict[shipNameList[i]]:
            ships1Dict[shipNameList[i]][shipName] = "-"

def finalSituation(playerList1, playerList2):
    """this function shows the latest status"""
    print("Final Information\n")
    print("Player1’s Board\t\t\t\tPlayer2’s Board")
    print("  A B C D E F G H I J\t\t\t  A B C D E F G H I J")

    outputFile.write("\nFinal Information\n\n")
    outputFile.write("Player1’s Board \t\t\tPlayer2’s Board\n")
    outputFile.write("  A B C D E F G H I J\t\t  A B C D E F G H I J\n")

    for i in range(10):
        for j in range(10):
            if playerList2[i][j] == "":
                playerList2[i][j] = "-"

    for i in range(10):
        for j in range(10):
            if playerList1[i][j] == "":
                playerList1[i][j] = "-"

    for row in range(10):
        if row == 9:
            print(str(row + 1), end="")
            outputFile.write(str(row + 1))
        else:
            print(str(row + 1), end=" ")
            outputFile.write(str(row + 1)+" ")
        for col in range(10):
            print(playerList1[row][col], end=" ")
            outputFile.write(playerList1[row][col]+" ")
        print("\t\t\t", end="")
        outputFile.write("\t\t")

        if row == 9:
            print(str(row + 1), end="")
            outputFile.write(str(row + 1))
        else:
            print(str(row + 1), end=" ")
            outputFile.write(str(row + 1)+" ")

        for col in range(10):
            print(playerList2[row][col], end=" ")
            outputFile.write(playerList2[row][col]+" ")
        print()
        outputFile.write("\n")

    shipsApperance(ships1Dict, player1ShipsPosition,player1PatrolBoat)
    shipsApperance(ships2Dict, player2ShipsPosition,player2PatrolBoat)

    print("\nCarrier\t      " + "%s\t\t\tCarrier       %s" % (player1ShipsPosition["C"], player2ShipsPosition["C"]))
    print("Battleship    " + "%s%s\t\t\t" % (player1ShipsPosition["B1"], player1ShipsPosition["B2"]) + "Battleship    %s %s" % (player2ShipsPosition["B1"], player2ShipsPosition["B2"]))
    print("Destroyer     " + "%s\t\t\t" % player1ShipsPosition["D"] + "        Destroyer     %s" % player2ShipsPosition["D"])
    print("Submarine     " + "%s\t\t\t" % player1ShipsPosition["S"] + "        Submarine     %s" % player2ShipsPosition["S"])
    print("Patrol Boat   " + "%s %s %s %s\t\t" % (patrolBoat1[0],patrolBoat1[1],patrolBoat1[2],patrolBoat1[3]) +
          "        Patrol Boat   %s %s %s %s" % (patrolBoat2[0],patrolBoat2[1],patrolBoat2[2],patrolBoat2[3]))

    outputFile.write("\nCarrier\t\t" + "%s\t\t\t\tCarrier\t\t%s" % (player1ShipsPosition["C"], player2ShipsPosition["C"]))
    outputFile.write("\nBattleship" + "\t%s%s\t\t\t\t" % (player1ShipsPosition["B1"], player1ShipsPosition["B2"]) + "Battleship\t%s %s" % (player2ShipsPosition["B1"], player2ShipsPosition["B2"]))
    outputFile.write(("\nDestroyer\t" + "%s\t\t\t\t" % player1ShipsPosition["D"] + "Destroyer\t%s" % player2ShipsPosition["D"]))
    outputFile.write(("\nSubmarine\t" + "%s\t\t\t\t" % player1ShipsPosition["S"] + "Submarine\t%s" % player2ShipsPosition["S"]))
    outputFile.write("\nPatrol Boat\t" + "%s %s %s %s\t\t\t" % (patrolBoat1[0],patrolBoat1[1],patrolBoat1[2],patrolBoat1[3]) + "Patrol Boat\t%s %s %s %s" %
                     (patrolBoat2[0],patrolBoat2[1],patrolBoat2[2],patrolBoat2[3]))
    outputFile.write("\n")
for i in range(len(takePlayer1Moves)):
    harf="ABCDEFGHIJ"
    sungedShip1Number = 0

    try:
        if len(takePlayer1Moves[i])<3:
            raise IndexError
        if (int(takePlayer1Moves[i].split(",")[0]) > 10) or (takePlayer1Moves[i].split(",")[1] not in harf):
            raise AssertionError
        player1Move(i)

    except AssertionError:
        print("AssertionError: Invalid Operation\n")
        outputFile.write("\nAssertionError: Invalid Operation\n")
        player1Move(i+1)

    except IndexError:
        print("IndexError: "+ takePlayer1Moves[i]+" something missing to move\n")
        outputFile.write("\nIndexError: "+ takePlayer1Moves[i]+" something missing to move\n")
        player1Move(i + 1)

    except:
        print("ValueError " + takePlayer1Moves[i]+" is not a correct move\n")
        outputFile.write("\nValueError " + takePlayer1Moves[i]+" is not a correct move\n")
        player1Move(i + 1)

    try:
        if len(takePlayer2Moves[i])<3:
            raise IndexError

        if (int(takePlayer2Moves[i].split(",")[0]) > 10) or (takePlayer2Moves[i].split(",")[1] not in harf):
            raise AssertionError
        player2Move(i)

    except AssertionError:
        print("AssertionError: Invalid Operation\n")
        outputFile.write("\nAssertionError: Invalid Operation\n")
        player2Move(i + 1)

    except IndexError:
        print("IndexError: "+ takePlayer2Moves[i]+" something missing to move\n")
        outputFile.write("\nIndexError: "+ takePlayer2Moves[i]+" something missing to move\n")
        player2Move(i + 1)

    except:
        print("ValueError " + takePlayer2Moves[i] + " is not a correct move\n")
        outputFile.write("\nValueError " + takePlayer2Moves[i] + " is not a correct move\n")
        player2Move(i + 1)

    for i in range(len(ships2Dict)):
        sungedShip1Number += ships1Dict[shipNameList[i]].count("-")

    sungedShip2Number = 0
    for i in range(len(ships2Dict)):
        sungedShip2Number += ships2Dict[shipNameList[i]].count("-")

    if sungedShip2Number == 27:
        player2Move(i)
        if sungedShip2Number == 27:
            print("It is a Draw!\n")
            outputFile.write("\nDRAW\n")
            patrolBoat2[0] = "X"
            patrolBoat2[1] = "X"
            patrolBoat2[2] = "X"
            patrolBoat2[3] = "X"
            finalSituation(player1List,player2List)
            break
        print("Player1 Wins!\n")
        outputFile.write("\nPlayer1 Wins!\n")
        finalSituation(player1List, player2List)
        break

    if sungedShip1Number == 27:
        print("Player2 Wins!\n")
        outputFile.write("\nPlayer2 Wins!\n")
        finalSituation(player1List, player2List)
        break





