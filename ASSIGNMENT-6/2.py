"""
Write a program to print all even numbers from 1 to N where you have to take N as input 
from the user. Note: Use while-loop OR for-loop, according to session flow.
Problem Constraints
A single line representing N
1 <= N <= 1000000
All even numbers from 1 to N are separated by spaces.
Input Format
Input 1:
5
Input 2:
10
Output Format
Output 1:
24 
Output 2:
2 4 6 8 10
"""
i = 1
n = int(input())
while (i <= n):
    if (i % 2 == 0):
        print(i, end=" ")
    i += 1
