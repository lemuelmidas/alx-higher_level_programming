#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first
    character
    """
    sentence_len = len(sentence)
    if sentence_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return ((sentence_len, first_char))
