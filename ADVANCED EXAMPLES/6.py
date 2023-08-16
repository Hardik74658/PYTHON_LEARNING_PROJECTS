# 6. Sort the above dictionary by the names of students.
data = {}
print("Enter Data For 10 Students")
for count in range(1,11):
    print(f"Enter Data For Student-{count} : ")
    temp=input("Enter Name : ")
    data[temp] = int(input("Enter Marks : "))
print(data)
print("Sorted Dictionary : ")
sorted_list = list(data.keys())
sorted_list.sort(key=str.lower)
sorted_dict={}
for keys in sorted_list:
    sorted_dict[keys]=(data[keys])
print(sorted_dict)