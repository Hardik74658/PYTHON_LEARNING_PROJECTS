"""8. Problem Description:
    A group of spammers is troubling Varun by calling on his mobile phone repeatedly. After a while, Varun observed a pattern that the mobile number from which the spammers call him is always lesser than his mobile number when compared on the number line. The mobile number of Varun is 1234880990. Given a mobile number as an input print True if the number belongs to the spammers else False.

    Input Format:
    The input will be a single integer representing a mobile number.

    Output Format:
    The output would be True if the condition holds else False

    Sample Input:
    9999999999

    Sample Output:
    False

    Note: All the mobile numbers in this problem are hypothetical
"""
varuns_mobile_number = 1234880990
mobile_number = int(input("Enter Mobile Number : "))
print(mobile_number < varuns_mobile_number)
