"""def avg(a):
    return sum(a)/len(a)


limit = int(input("Enter How Many Number's Avg You Want To Do"))
print(f"Enter {limit} numbers : ")
numList = []
for i in range(limit):
    num = int(input())
    numList.append(num)
print(avg(numList))


"""


def fact(n):
    if (n == 0):
        return 1
    else:
        return n*fact(n-1)


def avg(a, b, c, d, e):
    return (a+b+c+d+e)/5


print("Enter 5 Numbers : ")
average = 0
for i in range(5):
    num = int(input())
    average = average + avg(fact(num), 0, 0, 0, 0)

print(average)
# print(avg(fact(1), fact(2), fact(3), fact(4), fact(5)))
