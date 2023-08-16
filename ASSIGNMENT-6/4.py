"""
Print perfect squares
Problem Description
Given a number A. Print all perfect squares less than or equal to A. 
Notes - Perfect squares are integers whose square root is an integer.
Problem Constraints
1 <= A <= 104
Input Format
20
100
Output Format
A single line consisting of a integer A.
Example Input
Print perfect squares less than or equal to A in a single line in a space-separated manner.
Input 1:
Input 2:
Example Output
Output 1:
Output 2:
1 4 9 16
1 4 9 16 25 36 49 64 81 100

"""
n = int(input())
i = 1
while True:
    if i**2 <= n:
        print(i**2)
    else:
        break
    i += 1
