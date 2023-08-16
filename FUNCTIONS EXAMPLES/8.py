# 8. Write a function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.


def armstrong(num):
    power = len(str(num))
    temp = int(num)
    sum = 0
    for i in range(power):
        ld = temp % 10
        sum += ld**power
        temp = int(temp/10)
    if (sum == num):
        # print(f"{num} Is Armstrong number")
        print(num)


def armstrongInRange(start, end):
    for num in range(start, end):
        armstrong(num)


# num = int(input("Enter Number : "))
# armstrong(num)

start = int(input("Enter Starting Number :"))
end = int(input("Enter Ending Number :"))
armstrongInRange(start, end)
