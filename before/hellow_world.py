def collatz(number):
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        elif number %2 == 1:
            number = number * 3 + 1
        print(number)
    
def enterNumber():
    return input()


print("Please enter an integer")
try:
    number = int(input())
    collatz(number)
except ValueError:
    print("You should type a valid integer!!")

