"""7.Odd/Even - without 'if' statements
    Problem Description
    Given an integer n as input, print True if it is odd and False if it is even. Solve this question with the concepts taught in the Lecture on Operators. DO NOT USE IF/ELSE.

    Input Format:
    A single line input containing the integer.

    Output Format:
    A single-line boolean value.

    Input:
    2
    Output:
    False

    Example Explanation
    The output is False because 2 is even.
"""
num = int(input("Enter Number : "))
print(num % 2 != 0)
