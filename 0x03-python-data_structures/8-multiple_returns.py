#!/usr/bin/python3
def multiple_returns(sentence):
    '''Finds length and first character of a tuple

    Args:
        sentence: a tuple

    Returns: a tuple with the length of a string and its first character.
    '''
    return (len(sentence), None if len(sentence) == 0 else sentence[0])
