# 5. Ask user to give name and marks of 10 different students. Store them in dictionary.
data = {}
print("Enter Data For 10 Students")
for count in range(1,11):
    print(f"Enter Data For Student-{count} : ")
    temp=input("Enter Name : ")
    data[temp] = int(input("Enter Marks : "))
print(data)
