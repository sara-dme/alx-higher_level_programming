#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
if n % 10 < 6 and (n % 10) > 0:
    print(f"Last digit of {number} is {n} "
          f"and is less than 6 and not 0")
elif number == 0:
    print("Last digit of {} is {} and is 0".format(number, n))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, n))
