"""
4. Make a program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d
"""


def ap(n, a, d):
    return a + (n-1)*d


a = int(input("Enter First Term : "))
d = int(input("Enter Difference : "))
n = int(input("Enter Whic Term You Want : "))
print(f"{n}th Term Of AP : {ap(n, a, d)}")
