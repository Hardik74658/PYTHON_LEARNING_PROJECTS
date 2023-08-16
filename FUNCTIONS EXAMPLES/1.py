# 1. Ask two integers from user, add their factroials. Now ask two more integers from user and add their factorials too. calculate average of the factorials you computed. Now finally ask one last integer from user and add its factorial to the average.

def factorial(num):
    if (num == 0):
        return 1
    return (num*factorial(num-1))


def add(n1, n2):
    return n1+n2


def avg(n1, n2):
    return (n1+n2)/2


num1 = int(input("Enter Number-1:"))
print(f"Factorail of {num1} = {factorial(num1)}")
num2 = int(input("Enter Number-2:"))
print(f"Factorail of {num2} = {factorial(num2)}")
print(
    f"Add Of Factorials-1 & 2 is : {add(factorial(num1),factorial(num2))}")
num3 = int(input("Enter Number-3:"))
print(f"Factorail of {num3} = {factorial(num3)}")
num4 = int(input("Enter Number-4:"))
print(f"Factorail of {num4} = {factorial(num4)}")
print(
    f"Add Of Factorials-1 & 2 is : {add(factorial(num3),factorial(num4))}")

print(
    f"Average Of All Computed Factorials is : {avg(avg(factorial(num1),factorial(num2)),avg(factorial(num3),factorial(num4)))}")
num5 = int(input("Enter Number-5:"))
print(f"Factorail of {num5} = {factorial(num5)}")
print(
    f"Avg after adding last factorial : {add(factorial(num5),avg(avg(factorial(num1),factorial(num2)),avg(factorial(num3),factorial(num4))))}")
# print(factorial(5))
