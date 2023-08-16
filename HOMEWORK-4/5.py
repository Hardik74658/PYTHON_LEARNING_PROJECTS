A = int(input())
B = int(input())
C = int(input())
min = (A if A < B else B) if (A if A < B else B) < C else C
print(min)
