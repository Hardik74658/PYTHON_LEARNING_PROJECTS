"""
Count the digits – Poblem Description 
Take T (number of test cases) as input.
For each test case, take integer N as input and Print the count of digits of that number. 
Note: No of digits for number 0 is considered as 1.
Problem Constraints
1 <= T <= 100
0 <= N <= 100000000
Input Format
The first line is the number T which denotes the total number 
of test cases.
Next T lines contain an integer N for which you have to print 
the number of digits.
For T different Numbers, Print the number of digits in 
separate lines.
Input 1:
2
0
1
Input 2:
2
100
10101
Output Format
Output 1:
1
1
Output 2:
3
5
Example Input
Explanation 1:
0 and 1 both have only one digit. 
Explanation 2:
100 has three digits and 10101 has 5 digits.
"""
t = int(input())
i = 1
test_cases = []
while i <= t:
    test_cases.append(int(input()))
    i += 1
i = 0
while i < len(test_cases):
    temp = test_cases[i]
    cnt = 0
    if temp == 0:
        print(1)
    else:
        while temp > 0:
            temp //= 10
            cnt += 1
        print(cnt)
    i += 1
