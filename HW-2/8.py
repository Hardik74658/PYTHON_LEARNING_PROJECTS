"""8.Are the weights balanced?
    Problem Description:
    A weighing machine has two arms, a left arm, and a right arm. On both sides of the weighting machine we can put in weights and if both of those weights are equal, the arms of the machine will hang equally in the air, with none of them hanging below the other. This is hard to observe visually hence you are asked to write a program that takes in two weight values as input and outputs True if they will leave the machine balanced and False if they will leave the machine unbalanced.

    Input Format:
    The input will contain two lines denoting the weight values on the left and right arms of the machine

    Output Format:
    True if the machine is balanced. False if the machine is unbalanced.

    Input:
    64.0
    63.0
    Output:
    False
"""
weight_left = float(input("Enter Weight On Left Arm : "))
weight_right = float(input("Enter Weight On Right Arm : "))

print(weight_left == weight_right)
