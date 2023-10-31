#!/usr/bin/python3
for alphabets in range(97, 123):
    if alphabets == 101 or alphabets == 113:
        continue

    print("{:c}".format(alphabets), end='')
