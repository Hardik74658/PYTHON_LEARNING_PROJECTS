# 7. Write a function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.
def prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count = 1
            break
    if count == 0:
        print(num, end="\t")


def primeInRange(Start, End):
    for num in range(Start, End+1):
        prime(num)


start = int(input("Enter Starting : "))
end = int(input("Enter Ending : "))
primeInRange(start, end)
