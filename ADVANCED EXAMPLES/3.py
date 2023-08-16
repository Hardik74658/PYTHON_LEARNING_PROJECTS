# 3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
user_list = []
print("Enter 10 Integers")
for count in range(10):
    user_list.append(input(f"Enter Value-{count+1} : "))
print(user_list)
user_list.reverse()
print(user_list)

