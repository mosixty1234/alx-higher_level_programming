#!/usr/bin/python3 

def remove_characters(my_string, *chars):
    new_string = ""
    for char in my_string:
        if char.lower() not in [c.lower() for c in chars]:
            new_string += char
    return new_string

