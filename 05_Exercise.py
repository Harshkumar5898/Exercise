# Health Management System
# clint - Harry, Rohan and Hammad

# please make shour to make file name Harry_Exercise.txt, Harry_Dite.txt, Hammad_Exercise.txt, Hammad_Dite., Rohan_Exercise.txt, Rohan_Dite.txt

quit = False
while not quit:
    def getdate():
        import datetime
        return datetime.datetime.now()

    def Exercise(name):
        exercise = input("Enter what exercise you have done :- ")
        set = input("Enter number of sets you have done of this exercise :- ")
        rep = input("Enter number of reps you have done of this exercise :- ")
        with open(f"{name}_Exercise.txt", "a") as f:
            f.write(
                f"{time} - {name} does {set} set each of {rep} reps of {exercise}\n")

    def Dite(name):
        food = input("Enter what you eat :- ")
        amount = input(f"Enter in how much amount you consume {food} :-")
        with open(f"{name}_dite.txt", "a") as f:
            f.write(f"{time} - {name} ate {amount} {food}\n")

    def RetriveExercise():
        with open(f"{name}_Exercise.txt", "r") as f:
            print(f.read())

    def RetriveDite():
        with open(f"{name}_Dite.txt", "r") as f:
            print(f.read())

    time = getdate()
    print(time)

    print("===== Do you wand to log or retrive ======")
    print("          - Select 1 to log - ")
    print("        - Select 2 to retrive - ")
    print("------------------------------------------")
    a = int(input())

    print("======== Please select your name ======== ")
    print(" - Enter 1 if you are clint name Harry  - ")
    print(" - Enter 2 if you are clint name Rohan  - ")
    print(" - Enter 3 if you are clint name Hammad - ")
    print("------------------------------------------")
    n = int(input())
    if n == 1:
        name = "Harry"
    elif n == 2:
        name = "Rohan"
    elif n == 3:
        name = "Hammad"

    if a == 1:

        print(" ======== What do you want to lock ========")
        print(" - Select 1 if you want to log Exercise - ")
        print("   - Select 2 if you want to log dite -   ")
        print("-------------------------------------------")
        l = int(input())
        if l == 1:
            Exercise(name)
        elif l == 2:
            Dite(name)
    if a == 2:

        print(" ======== What do you want to retrive ========")
        print(" - Select 1 if you want to retrive Exercise - ")
        print("   - Select 2 if you want to retrive dite -   ")
        print("----------------------------------------------")
        l = int(input())
        if l == 1:
            RetriveExercise()
        elif l == 2:
            RetriveDite()

    print("\nDo you wand to quit or want to log or retrive something")
    print("Please enter y to quit or n to continue")
    q = input()
    if q == "y" or q == "Y":
        quit = True
