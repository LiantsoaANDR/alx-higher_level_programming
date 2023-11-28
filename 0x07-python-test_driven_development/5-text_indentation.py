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
    flag = True
    for char in text:
        if not flag:
            if char != ' ':
                flag = True
            else:
                continue
        if char not in indentation:
            print(char, end="")
        else:
            print("{}\n".format(char))
            flag = False
