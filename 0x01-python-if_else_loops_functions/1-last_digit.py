#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10

if number <= 0:
    last_num = last_num * -1

if last_num > 5:
    output = "greater than 5"
elif last_num == 0:
    output = "0"
else:
    output = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, last_num, output))
