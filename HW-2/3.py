"""3.	Floors and Ceilings
    Problem Description:
    The floor function floor(x) is defined as the greatest integer less than or equal to the given number.
    For example, floor(7.64)=7.
    Likewise, the ceiling function ceil(x) is defined as the smallest integer greater than or equal to the given number.
    For example, ceil(7.64)=8.
    Given a number x as input, output its floor(x) and ceil(x) values.

    Note: Assume that the input will never be an integer.

    Input Format:
    One line float value

    Output Format:
    Print two integers, first one denoting the floor value and second one the ceiling value of the given number.
    
    Input:
    7.64
    Output:
    7
    8

    Example Explanation:
    The greatest integer that is less than or equal to 7.64 is clearly 7.
    The smallest integer that is greater than or equal to 7.64 is clearly 8.
"""
import math
num = float(input("Enter Number : "))
# print(f"Floor Of Number : {math.floor(num)}")
# print(f"Ceil Of Number : {math.ceil(num)}")


floor = int(num)
ceil = int(num+1)
print(f"Floor Of Number : {floor}")
print(f"Ceil Of Number : {ceil}")
