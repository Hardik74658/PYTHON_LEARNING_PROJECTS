month = int(input())

if month == 2:
    print(28)

else:

    if month < 8:
        if month % 2 != 0:
            print(31)
        else:
            print(30)
    else:
        if month % 2 == 0:
            print(31)
        else:
            print(30)
