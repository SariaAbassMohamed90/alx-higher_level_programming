#!/usr/bin/python3
"""defining appends_write function"""


def append_write(filename="", text=""):
    """appends filename with utf-8"""
    with open(filename, 'a', encodeing="utf-8") as f:
        return f.write(text)
