# chr: ascii to character
"""
print(chr(65))
"""
# eval:
"""
a = "print('Hello World!')"
eval(a)
# print(a)

b = "int(input(f'Enter a number: '))"
p = eval(b)
print(p)
"""

# isinstance
"""
a = float(input("a: "))
b = 25
print(isinstance(a, int))
print(isinstance(b, int))
"""

# next
"""
marks = [
    ["Sr.", "Name", "Sub-1", "Sub-2"],
    [1, "Darshan", 30, 31],
    [2, "Rishi", 29, 33],
    [3, "Jay", 32, 32]
]
# print(marks[0])
title = next(marks)
print(marks)
"""

# pow: as using **

# round
"""
print(round(3.4))           # 3
print(round(3.7))           # 4
print(round(3.141569, 2))   # 3.14
print(round(3.141569, 3))   # 3.142
print(round(3.142596))      # 3
print(round(3.142596, 0))   # 3.0
print(round(4568.239, 2))   # 4568.24
print(round(4568.239, 0))   # 4568.0
print(round(4568.239, -1))  # 4570
print(round(4568.239, -3))  # 5000

print(round(-3.4))
print(round(-4.8))
"""
# floor & ceil
"""
print(math.floor(5.9))
print(math.floor(3.001))

print(math.ceil(3.0001))

print(math.floor(-2.2))
print(math.floor(-3.2))

print(math.ceil(-2.2))
print(math.ceil(-3.2))
"""
# zip
"""
roll_no = [1, 2, 3, 4, 5]
names = ["A", "B", "C", "D", "E"]
print(list(zip(roll_no, names)))
percentage = [75, 82, 93, 58, 90]
print(list(zip(roll_no, names, percentage)))
"""

# map


# import math
# def factorial(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f


# numbers = [2, 3, 4, 5, 6, 7, 8, 9]

# # use the above function and create another list named 'factorials' that contains factorials of all the members of list 'numbers'
# factorial_list = []
# for num in numbers:
#     fact = factorial(num)
#     factorial_list.append(fact)
# print(factorial_list)


# HW


# HW - 2

# def hugeTransactions(transaction):
#     return abs(transaction) >= 50000


# transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
# bigTransactions = []
# for transaction in transactions:
#     if hugeTransactions(transaction):
#         bigTransactions.append(transaction)
# print(bigTransactions)


def absoluteTotal(a, b):
    return abs(a) + abs(b)


transactions = [1000, 25000, -31000, -60000, 40000, 49900, 120000, -70000]
# april = [10, -10, 20, -20]
# print(absoluteTotal(10, -10))
# Use above function and the list of transaction, use the topics taught (especially for loop) and write your code below to get total amount transacted.
total_Transaction = 0
for transaction in transactions:
    total_Transaction = absoluteTotal(transaction, total_Transaction)
print(total_Transaction)
