"""2.Pac-man
Problem Description
In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game. 
You have to answer whether the Pac-Man loses or not.
Your are given the following integer inputs (0 / 1) one in each line: 
1. Does the Pac-Man have a power pellect active?
2. Is the Pac-Man touching a ghost?
The Pac-Man loses if it is touching a ghost and does not have a power pellet active. 
Input Format
There are 2 lines in the input.
The first line indicates if the Pac-Man has a power pellet active (1 for yes, 0 for no)
The second line indicates if the Pac-Man is touching a ghost (1 for yes, 0 for no)


Output Format
Print 1 if the Pac-Man loses else 0.
Example Input
Input 1:-
0
1

Input 2:-
0
0
Example Output
1
0
"""
power_pellet = int(input())
touch_ghost = int(input())


if power_pellet:
    if touch_ghost:
        print(0)
    else:
        print(1)
else:
    if touch_ghost:
        print(1)
    else:
        print(0)
