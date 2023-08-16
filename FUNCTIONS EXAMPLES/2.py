# 2. Write a function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.

def prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count = 1
            print(f"{num} is Not A Prime Number")
            break
    if count == 0:
        print(f"{num} is A Prime Number")


num = int(input("Enter a Number : "))
prime(num)
