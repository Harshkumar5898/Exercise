# Exercise 2 --> Faulty Calculator
# 45 * 3 = 555 , 56 + 9 = 77, 56/6 = 4

from ast import operator


dict = {"45*3" : "555",
        "56+9" : "77",
        "56/6" : "4"}

num1 = input("Enter your first number : ")
operator = input("Enter operator : ")
num2 = input("Enter your second number : ")

a = num1+operator+num2
reverse = num2+operator+num1

if a in dict:
    print(dict[a])

elif reverse in dict:
    print(dict[reverse])

else:
    if operator == "+":
        print(int(num1) + int(num2))
    if operator == "-":
        print(int(num1) - int(num2))
    if operator == "*":
        print(int(num1) * int(num2))
    if operator == "/":
        print(int(int(num1) / int(num2)))
