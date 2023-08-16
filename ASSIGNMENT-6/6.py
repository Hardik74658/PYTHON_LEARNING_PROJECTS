"""6.   Multiples of 4
Problem Description
Given an integer input N, print all multiples of 4 less than or equal to N. 
Problem Constraints
22
Input Format
1 <= N <= 10000
Output Format
Single line containing an integer N.
Example Input
Example Output
Space separated integers representing multiples of 4 less than or equal to N.
Example Explanation
4 8 12 16 20
1 * 4 = 4 
2 * 4 = 8 
3 * 4 = 12 
4 * 4 = 16 
5 * 4 = 20
All are multiples of 4 less than 22"""

n = int(input())
i = 1
while 4*i <= n:
    print(4*i, end=" ")
    i += 1
