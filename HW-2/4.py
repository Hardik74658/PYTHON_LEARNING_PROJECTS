"""4. Multiply Chain
    Problem Description:
    Given a number n as input, multiply it with the number (n-1) and (n-2) and print the resultant output.

    Input Format:
    A single line containing an integer.

    Output Format:
    A single line output according to the problem description.

    Input:
    10
    Output:
    720
"""
num = int(input("Enter A Number : "))
print(num*(num-1)*(num-2))
