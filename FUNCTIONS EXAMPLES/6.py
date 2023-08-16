# 6. Make a function that checks whether the given number is a perfect number or not. Make a program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.

def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        # print(f"{num} is a perfect number")
        print(num)
    # else:
    #     print(f"{num} is not a perfect number")


# perfect(6)

def perfectInRange(start, end):
    for num in range(start, end):
        perfect(num)


start = int(input("Enter Starting Of Range : "))
end = int(input("Enter Ending Of Range : "))
perfectInRange(start, end)
