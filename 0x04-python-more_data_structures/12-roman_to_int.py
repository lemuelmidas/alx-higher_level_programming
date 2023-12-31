#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_list = list(roman_string.upper())
    result = 0
    prev = 0
    for letter in roman_list:
        if letter in roman:
            result += roman[letter]
            if roman[letter] > prev:
                result -= prev * 2
            prev = roman[letter]
        else:
            return (0)
    return (result)
