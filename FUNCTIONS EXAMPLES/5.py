# 5. Develop a program that uses a function to find nth term of an geometric progression whose first term is 'a' & common ratio is 'r'.

def gp(a, r, n):
    return a*(r**(n-1))


a = int(input("Enter First Term : "))
r = int(input("Enter Ratio : "))
n = int(input("Enter Whic Term You Want : "))
print(f"{n}th Term Of GP : {gp(a,r,n)}")
