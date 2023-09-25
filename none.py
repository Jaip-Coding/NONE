################################
# NONE v1.0 Compiler in Python #
################################

import re

TOKENS = "abcdefghijklmnopqrstuvwxyz"
TOKENS_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_TOKENS = '_.!?-:()@#'
MATH_TOKENS = "$+-*/=%^<>"

USER_INPUT = input()

USER_TOKENS = re.split(r'(\d|\D)', USER_INPUT)

for token in USER_TOKENS:
    USER_TOKENS.remove("")

INDEX = 0
LAST_TOKEN = None
TOKENS_LIST = [*TOKENS]
TOKENS_CAPS_LIST = [*TOKENS_CAPS]
SPECIAL_TOKENS_LIST = [*SPECIAL_TOKENS]
MATH_TOKENS_LIST = [*MATH_TOKENS]
IS_NUMBER = False
NUMBER_INDEX = 0
IS_SPECIAL = False
SPECIAL_INDEX = 0
IS_MATH = False
MATH_INDEX = 0
OUTPUT = ""

for token in USER_TOKENS:
    if IS_NUMBER:
        if LAST_TOKEN == "+":
            if token == "+":
                NUMBER_INDEX += 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                NUMBER_INDEX += 5
                LAST_TOKEN = None
        elif LAST_TOKEN == "-":
            if token == "-":
                NUMBER_INDEX -= 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                NUMBER_INDEX -= 5
                LAST_TOKEN = None
        elif LAST_TOKEN is None:
            #print("TEST")
            #print(token)
            if token == "+":
                LAST_TOKEN = "+"
            elif token == "-":
                LAST_TOKEN = "-"
            elif token == ")":
                LAST_TOKEN = None
                OUTPUT += str(NUMBER_INDEX)
                NUMBER_INDEX = 0
                IS_NUMBER = False
        #print(NUMBER_INDEX)
        continue
    
    if IS_SPECIAL:
        if LAST_TOKEN == "+":
            if token == "+":
                SPECIAL_INDEX += 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                SPECIAL_INDEX += 5
                LAST_TOKEN = None
        elif LAST_TOKEN == "-":
            if token == "-":
                SPECIAL_INDEX -= 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                SPECIAL_INDEX -= 5
                LAST_TOKEN = None
        elif LAST_TOKEN is None:
            if token == "+":
                LAST_TOKEN = "+"
            elif token == "-":
                LAST_TOKEN = "-"
            elif token == ")":
                LAST_TOKEN = None
                OUTPUT += SPECIAL_TOKENS_LIST[SPECIAL_INDEX]
                SPECIAL_INDEX = 0
                IS_SPECIAL = False
        continue
    
    if IS_MATH:
        if LAST_TOKEN == "+":
            if token == "+":
                MATH_INDEX += 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                MATH_INDEX += 5
                LAST_TOKEN = None
        elif LAST_TOKEN == "-":
            if token == "-":
                MATH_INDEX -= 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                MATH_INDEX -= 5
                LAST_TOKEN = None
        elif LAST_TOKEN is None:
            if token == "+":
                LAST_TOKEN = "+"
            elif token == "-":
                LAST_TOKEN = "-"
            elif token == ")":
                LAST_TOKEN = None
                OUTPUT += MATH_TOKENS_LIST[MATH_INDEX]
                MATH_INDEX = 0
                IS_MATH = False
        continue
    
    if LAST_TOKEN is not None:
        if LAST_TOKEN == "+":
            if token == "+":
                INDEX += 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                INDEX += 5
                LAST_TOKEN = None
            elif token == "X" or token == "x":
                INDEX += 10
                LAST_TOKEN = None
            elif token == "T" or token == "t":
                INDEX += 20
                LAST_TOKEN = None
        elif LAST_TOKEN == "-":
            if token == "-":
                INDEX -= 1
                LAST_TOKEN = None
            elif token == "V" or token == "v":
                INDEX -= 5
                LAST_TOKEN = None
            elif token == "X" or token == "x":
                INDEX -= 10
                LAST_TOKEN = None
            elif token == "T" or token == "t":
                INDEX -= 20
                LAST_TOKEN = None
        elif LAST_TOKEN == "^":
            if token == "P" or token == "p":
                OUTPUT += TOKENS_CAPS_LIST[INDEX - 1]
            LAST_TOKEN = None
        elif LAST_TOKEN == "n":
            if token == "(":
                LAST_TOKEN = "n("
        elif LAST_TOKEN == "n(":
            IS_NUMBER = True
            if token == "+":
                LAST_TOKEN = "+"
        elif LAST_TOKEN == "s":
            if token == "(":
                LAST_TOKEN = "s("
        elif LAST_TOKEN == "s(":
            IS_SPECIAL = True
            if token == "+":
                LAST_TOKEN = "+"
        elif LAST_TOKEN == "m":
            if token == "(":
                LAST_TOKEN = "m("
        elif LAST_TOKEN == "m(":
            IS_MATH = True
            if token == "+":
                LAST_TOKEN = "+"
    elif LAST_TOKEN is None:
        if token == "+":
            LAST_TOKEN = "+"
        elif token == "-":
            LAST_TOKEN = "-"
        elif token == "P" or token == "p":
            OUTPUT += TOKENS_LIST[INDEX - 1]
        elif token == "^":
            LAST_TOKEN = "^"
        elif token == "n" or token == "N":
            LAST_TOKEN = "n"
        elif token == "s" or token == "S":
            LAST_TOKEN = "s"
        elif token == "m" or token == "M":
            LAST_TOKEN = "m"
        elif token == "_":
            OUTPUT += " "
            LAST_TOKEN = None
        elif token == "c":
            INDEX = 0
            LAST_TOKEN = None

print(OUTPUT)
