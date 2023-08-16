N = int(input())
if N < 5*10**5:
    print("None")
elif N < 10**6:
    print("Gold")
elif N < 10**7:
    print("Platinum")
else:
    print("Diamond")
