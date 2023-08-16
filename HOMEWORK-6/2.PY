"""
Easy Power
Problem Description
You are given two integers A and B. You have to find the value of AB. 
NOTE: The value of AB  will always be less than or equal to 109. 
You are not allowed to use ** operator or pow() function. 
Problem Constraints
1 <= A, B <= 1000
Input Format
2
3
1
10
Output Format
First line of the input contains a single integer A. 
Second line of the input contains a single integer B.
8
Example Input
1
Input 1:
Print a single integer in single line.
Input 2:
Example Output
Output 1:
Output 2:
"""


a = int(input())
b = int(input())

cnt = 1
while cnt < b:
    a *= 2
    cnt += 1
print(a)
