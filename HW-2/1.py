"""1. Numerical Derivative
    Problem Description:
    The derivative of a function is a value that tells us how much the output of a mathematical function would change, if we were to make a very, very tiny change in its input. In mathmetical terms, the limit definition of a derivative is defined as: limo Where x and hare both inputs to the h
    function f. You can safely ignore the lim part in the expression.
    Given the values of x and your task is to evaluate the expression for the function f(x) = 3x² + 2 and print the value obtained.

    Input Format:
    The input will contain two numbers.
    The first line will be the x value.
    The second line will be the h value.

    Output Format:
    The output would be a single line float value of the expression in problem description.
    
    Input:
    1
    1
    Output:
    9.0

    Note: The value of hwill always be more than for this problem.
"""


def f(x):
    return 3*x*x + 2


x = int(input())
h = int(input())
print((f(x+h)-f(x))/h)
