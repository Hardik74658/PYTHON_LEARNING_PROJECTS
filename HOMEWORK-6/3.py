"""
Sum the digits – DO NOT USE FOR LOOP
Problem Description
Take T (number of test cases) as input. For each test case, take integer N as input and 
Print the sum of digits of that number.
Problem Constraints
1 <= T <= 1000
0 <= N <= 100000000
Input Format
The first line is T which means the total number of test 
cases. Each of the next T lines contain an integer N.
Input 1:
2
5
1001 
Input 2:
2
123
1589
Output Format
Output 1:
5
2
Output 2:
6
23
Example Input
T lines each containing one integer representing the sum of 
the digits of the input integer.
Example Output
Example Explanation
Explanation 1:
5 has only 1 digit hence sum is 5. 
Sum(1001) = 1+0+0+1 = 2. 
Explanation 2:
Sum(123) = 1+2+3 = 6. 
Sum(1589) = 1+5+8+9 = 23.
"""
t = int(input())
test_cases = []
i = 1
while i <= t:
    test_cases.append(int(input()))
    i += 1
i = 0
while i < len(test_cases):
    temp = test_cases[i]
    sum = 0
    while temp > 0:
        ld = temp % 10
        sum += ld
        temp //= 10
    print(sum)
    i += 1
