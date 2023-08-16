"""
4. Pr-oblem Description: Given two names A and B as input, print "A says Hi to B", where A and B are the names in input.

    Problem Constraints
    1 <= len(A), len(B) <= 15
    Characters in A and B are in lowercase English Alphabets.

    Input Format:
    There are two input lines
    The first line has a string A.
    The second line has a string B.

    Output Format:
    Print in a single line A says Hi to B.

    Examples 
    Input:
    Ram
    Shyam

    Output:
    Ram says Hi to Shyam
"""
name1 = input("Enter 1st Name : ")
name2 = input("Enter 2nd Name : ")

name1 = name1.capitalize()
name2 = name2.capitalize()

print(f"{name1} says Hi to {name2}")
