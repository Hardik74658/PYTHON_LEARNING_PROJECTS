num = int(input())
if num % 3 == 0:
    if num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")

else:
    if num % 5 == 0:
        print("Buzz")
