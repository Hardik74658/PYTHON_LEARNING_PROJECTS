"""5.Module Trouble
    Problem Description:
    Shikha is trying to solve a hard math problem in which she is required to take the mod of a number x with y quite frequently. Given two numbers x and y write a program that helps Shikha do this easily. Assume that the value of y is always greater than 0.

    Input Format:
    Two lined inputs. The first line denotes the x value and the second one the y value.

    Output Format:
    Single number which is the mod of x with y.

    Input:
    100
    11
    Output:
    1
 """
x = int(input("Enter x : "))
y = int(input("Enter y : "))
print(f"Mod Of x with y : {x%y}")
