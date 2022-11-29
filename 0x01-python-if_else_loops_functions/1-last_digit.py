#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
print("Last digit of the {number} is {digit} and is greater than 5"
elif digit == 0:
print("Last digit of the {number} is {digit} and is 0"
else:
print("Last digit of the {number} is {digit} and s less than 6 and not 0"
