"""
.   Odd Game
Problem Description
Write a program to print all odd numbers from 1 to N where you have to take N as input 
from user. Here N is inclusive.
Problem Constraints
1 <= N <= 2000000
Input Format
A single line representing N
5
10
Output Format
All odd numbers from 1 to N separated by spaces.
Example Input
Input 1:
Input 2:
Example Output
Output 1:
Output 2:
1 3 5
1 3 5 7 9
"""

n = int(input())
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end="")
    i += 1
