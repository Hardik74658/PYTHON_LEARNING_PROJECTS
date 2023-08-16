# 7. Sort the dictionary in ex-5 by the marks.
data = {}
print("Enter Data For 10 Students")
# for count in range(1,11):
#     print(f"Enter Data For Student-{count} : ")
#     temp=input("Enter Name : ")
#     data[temp] = int(input("Enter Marks : "))
print(data)
print("Sorted Dictionary : ")
sorted_list = list(data.values())
sorted_list.sort()
sorted_dict={}
for values in sorted_list:
    for keys in data:
        if values == data[keys]:
            sorted_dict[keys]=values
print(sorted_dict)