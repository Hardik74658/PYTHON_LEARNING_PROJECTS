x = int(input())
y = int(input())
if (x + y) % 5 == 0:
    x += 1
    y += 1
elif x % 2 == 0 and y % 2 != 0:
    y += 1
elif y % 2 == 0 and x % 2 != 0:
    x += 1
print(x)
print(y)
