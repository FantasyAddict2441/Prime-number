import math
def factorals(num):
    prime = 0
    print("Factorals:")
    #num2 = float(num)
    square = int(math.sqrt(num)) + 1

    for i in range(2, square):
        if (num % i) == 0:
            prime = 1
            x = int(num / i)
            print(f"{i} x {x}")
    
    if prime == 0:
        print(f"{num} is a prime number!")

num = int(1)

while(num != 0):
    num = int(input("Enter a number: "))
    if num == 0:
        break
    factorals(num)
    print()