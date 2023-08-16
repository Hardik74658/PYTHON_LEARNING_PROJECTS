"""1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.
for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']"""

list1 = ['no bun', 'bug bun bug bun bug bug',
         'bunny bug', 'buggy bug bug buggy']
count_list = []
string = input("Enter String For Sorting : ")
for sub_str in list1:
    count_list.append(sub_str.count(string))
    print(sub_str.count(string))
# count_list.sort(reverse=True)
print(count_list)
for num in count_list:
    list1[count_list.index(num)]=(str(num).join(list1))
# list1.sort()
print(list1)
