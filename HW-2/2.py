"""2.Is the third one greater?
    Problem Description:
    Given three integer values as input, your task is to print True if the third number is greater than the first two else False.

    Input Format:
    Input will contain three lines denoting three integer values.

    Output Format:
    The output would be True if the condition holds else False.

    Input:
    1
    2
    3
    Output:
    True

    Explanation:
    Here 3 is greater than 1 and 3 is also greater than 2 and hence the output is True.
"""
num1 = int(input("Enter Num-1 : "))
num2 = int(input("Enter Num-2 : "))
num3 = int(input("Enter Num-3 : "))
print(num3 > num1 and num3 > num2)
