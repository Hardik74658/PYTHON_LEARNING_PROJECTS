# 3. Write a function to find average of 5 given numbers and a main program that takes 5 integers from user, uses the factorial function to find factorial of each one of them and using average function prints the average of factorials of them.
def fact(num):
    if (num == 0):
        return 1
    return (num*fact(num-1))


def avg(n1, n2, n3, n4, n5):
    return (n1+n2+n3+n4+n5)/5


num1 = int(input("Enter Number-1 : "))
print(f"Factorial-1 : {fact(num1)}")
num2 = int(input("Enter Number-2 : "))
print(f"Factorial-2 : {fact(num2)}")
num3 = int(input("Enter Number-3 : "))
print(f"Factorial-3 : {fact(num3)}")
num4 = int(input("Enter Number-4 : "))
print(f"Factorial-4 : {fact(num4)}")
num5 = int(input("Enter Number-5 : "))
print(f"Factorial-5 : {fact(num5)}")

print(
    f"Average Of Factorials : {avg(fact(num1),fact(num2),fact(num3),fact(num4),fact(num5))}")
