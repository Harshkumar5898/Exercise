import random
from timeit import repeat

randNo = random.randint(1,100)
userNo = None
guesses = 0

print("-------Welcome to guess number game-------")

while userNo != randNo :
    if guesses == 10:
        print("You lost, No chance left")
        break

    userNo = input("Enter your guess - ")
    if not userNo.isnumeric():
        print("Please enter a valid integer")
        continue
    guesses += 1
    userNo = int(userNo)

    if userNo == randNo:
        print("|-|congrulation, Your guess is correct|-|")
        print(f"      You win the game in {guesses} guesses      ")
    else:
        if userNo>randNo and guesses != 10:
            print("Your number is greater than original number, please enter a smaller number")
        elif userNo<randNo and guesses != 10:
            print("Your number is smaller than original number, please enter a greater number")