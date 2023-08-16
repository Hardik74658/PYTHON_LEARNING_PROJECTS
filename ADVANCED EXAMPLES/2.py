"""2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not."""

user_set = set()
print("Enter Values You Want In Set And Enter STOP If You Dont Want To Add Any Other Values")
while True:
    temp = input("Value : ")
    if temp.lower() == "stop":
        break
    else:
        user_set.add(temp)
check = input("Enter Value You Want To Check : ")
set(check)
if user_set.issuperset(check):
    print(f"{check} is Present In Set")
else:
    print(f"{check} is not Present In Set")
