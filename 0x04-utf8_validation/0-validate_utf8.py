#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    bytes_to_follow = 0
    for char in data:
        binary = format(char, '#010b')[-8:]
        if bytes_to_follow == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                bytes_to_follow = 1
            elif binary.startswith('1110'):
                bytes_to_follow = 2
            elif binary.startswith('11110'):
                bytes_to_follow = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            bytes_to_follow -= 1
    return bytes_to_follow == 0