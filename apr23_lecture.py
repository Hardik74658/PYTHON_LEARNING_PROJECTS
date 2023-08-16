# Scope of a variable, local variables, global variables & global keyword
"""
var1 = 10                           # global variable

def func1():
    global var1
    var1 += 1
    print("var1 from func1 =", var1)
    # print("var2 from func1 =", var2)
    var3 = 30                       # local variable: variable with local scope
    print("var3 from func1 =", var3)
    def subFunc():                  # local function: function with local scope
        print("var3 from subFunc =", var3)
    subFunc()
    return var1

def func2():
    global var1, var2
    print("var2 from func2 =", var2)
    # print("var3 from func2 =", var3)

print("var1 from main =", var1)
var1 += 1
a = func1()
var2 = 20                           # global variable for all the functions CALLED AFTER THIS POINT
func2()
# subFunc()
print("var1 from main =", var1)

# print("var3 from main =", var3)
"""

# A typical programming sequence:
"""
import statements

global constants & variables

functions

main
"""

# lambda functions
# def cube(x):
#     return x ** 3
"""
cube = lambda x : x ** 3
print(cube(3))

def sqrt(n):
    return n ** 0.5

sqrt = lambda n : n ** 0.5

def avg(a, b):
    return (a + b)/2

avg = lambda a, b : (a + b)/2

def root():
    return float(input("number: ")) ** 0.5

root = lambda : float(input("number: ")) ** 0.5
print(root())
"""

# lambda a, b : (a + b)/2
# lambda : float(input("number: ")) ** 0.5

# some useful built in functions

n = [10, 32, 34, 50, 62, 73, 89, 93, 10]
# n = [1, 2, 34, 5, 6, 7, 8, 9, 10, "Vivek"]
# print(sum(n))
# name = ["Vivek", "Prajapati"]
# print(sum(name, " "))

# print(sum(n, 1000))

x1 = 3
y1 = 4

x2 = -2
y2 = -4

distance = abs(x1 - x2) + abs(y1 - y2)
print(distance)

print("Absolute of 5:", abs(5))
print("Absolute of -5:", abs(-5))

# Next Class: Some more Built-in useful functions, Recursive functions

# HW:
"""
















"""
