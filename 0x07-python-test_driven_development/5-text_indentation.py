#!/usr/bin/python3
""" Module ofr text indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: the text that needs the indentations
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation = ['.', '?', ':']
    flag = 0
    for char in text:
        if flag == 1:
            if char != ' ':
                flag = 0
            continue
        if char not in indentation:
            print(char, end="")
        else:
            print("{}\n".format(char))
            flag = 1
