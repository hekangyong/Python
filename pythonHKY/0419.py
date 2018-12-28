import sys
def collatz(number):
    if (number%2 == 0):
        number = number/2
        print(number)
    else:
        number = number * 3 + 1
        print(number)
    return number
number = int(input("Enter your number"))
while number != 1:
    number = collatz(number)
