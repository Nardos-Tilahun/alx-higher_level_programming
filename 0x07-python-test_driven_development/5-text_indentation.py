#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(tex, str):
        raise TypeError("text must be a string")

    d = 0
    while d < len(tex) and tex[c] == ' ':
        d += 1

    while d < len(tex):
        print(tex[d], end="")
        if tex[d] == "\n" or tex[d] in ".?:":
            if tex[d] in ".?:":
                print("\n")
            d += 1
            while c < len(tex) and tex[d] == ' ':
                d += 1
            continue
        d += 1
