"""
9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""

dict_of_list = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list_of_dict = []
temp={}
for index in range(4):
    temp.clear()
    for key in dict_of_list:
        temp[key]=dict_of_list[key][index]
    list_of_dict.append(temp.copy())
print(list_of_dict)
