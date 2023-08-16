
cache_memory = {}


def fibo(n):
    if n in cache_memory:
        return cache_memory[n]
    if n == 1 or n == 2:
        cache_memory[n] = 1
        return 1
    else:
        term = fibo(n-1) + fibo(n-2)
        cache_memory[n] = term
        return term


num = int(input("Enter Number : "))
print(fibo(num))

for i in range(1, num+1):
    print(fibo(i))
