import random

totalrounds = 1
compwins = 0
yourwins = 0

def round():
    if comp == player:
        return None
    elif comp == "Snake":
        if player == "Water":
            return 0
        elif player == "Gun":
            return 1
    elif comp == "Water":
        if player == "Gun":
            return 0
        elif player == "Snake":
            return 1
    elif comp == "Gun":
        if player == "Snake":
            return 0
        elif player == "Water":
            return 1
                
def thisroundwin():
    global compwins
    global yourwins
    print("|---------------------------------|")
    if roundwin == None:
        print("|        This Round Is Tie        |")
    elif roundwin == 1:
        print("|        You Win This Round       |")
    elif roundwin == 0:
        print("|       You Lose This Round       |")

while totalrounds <=10:

    compchoise = ["Snake", "Water", "Gun"]
    comp = random.choice(compchoise)

    print("|---------------------------------|")
    print(f"| ROUND - {totalrounds}                       |")
    print("|======= Enter your choise =======|")
    print("|  - Selec (s) to chose Snake -   |")
    print("|  - Selec (w) to chose Water -   |")
    print("|  - Selec (g) to chose Gun   -   |")
    print("|---------------------------------|")
    playerchoise = input("                 ")
    
    if playerchoise == "s" or playerchoise == "S":
        player = "Snake"
    elif playerchoise == "w" or playerchoise == "W":
        player = "Water"
    elif playerchoise == "g" or playerchoise == "G":
        player = "Gun"
    

    roundwin = round()
    thisroundwin()
    

    if roundwin == 1:
        yourwins += 1
    elif roundwin == 0:
        compwins += 1


    totalrounds += 1

    print(f"|      Computer choise - {comp}      |")
    print(f"|      Your choise - {player}        |") 
    print(f"|         SCORE  [{yourwins} - {compwins}]          |")
    print("|---------------------------------|")
    print("\n\n\n")


def Gamewinner():
    print("|---------------------------------|")
    if compwins == yourwins:
        print("|        This Match Is Tie        |")
    elif yourwins > compwins:
        print("|       You Win This Match        |")
    elif compwins > yourwins:
        print("|       You Lose This Match       |")

Gamewinner()
print(f"|       Final Score  [{yourwins} - {compwins}]      |")
print("|---------------------------------|")