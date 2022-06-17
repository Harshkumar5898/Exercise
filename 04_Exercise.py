def stars(n):
    for i in range(n):
        print("*" * (i+1))

def reverse(n):
    # while n>0:
    #     print("*" * (n))
    #     n -= 1
     for i in range(n, 0, -1):
        print("*" * i)


n = int(input("Enter number of rows :- "))
a = int(input("Enter 0 for false or 1 for true :- "))
bool = None

if a == 0:
    bool = False
elif a == 1:
    bool = True

if bool:
    stars(n)
elif not bool:
    reverse(n)