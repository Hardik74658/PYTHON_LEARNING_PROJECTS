"""
1. Problem Description: Given a name A as input. Print "Hello A", where A is the name in input.

    Problem Constraints:
    1 <= len(A) <= 15
    Characters in A are in lowercase English Alphabets.

    Input Format:
    There is a single input line, which is the string A.

    Output Format:
    Print in a single line "Hello A" without quotes.

    Examples 
    Input 1:
    Ram
    Output 1:
    Hello Ram

    Input 2:
    Shyam
    Output 2:
    Hello Shyam
"""
name = input("Enter Name : ")
while len(name) > 15:
    print("Length of Name must be less than 15 characters")
    name = input("Enter Name : ")

name = name.capitalize()
print("Output : ")
print(f"Hello {name}")
