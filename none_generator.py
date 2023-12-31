######################
# NONE 1.0 Generator #
######################

import re

TOKENS = "abcdefghijklmnopqrstuvwxyz"
TOKENS_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

USER_INPUT = input()

if USER_INPUT == "file:" or USER_INPUT == "file" or USER_INPUT == "File:" or USER_INPUT == "File" or USER_INPUT == "FILE:" or USER_INPUT == "FILE":
    USER_INPUT = input()
    with open(USER_INPUT, 'r') as file:
        USER_INPUT = file.read()

USER_TOKENS = re.split(r'(\d|\D)', USER_INPUT)

for token in USER_TOKENS:
    USER_TOKENS.remove("")

OUTPUT = ""
INDEX = 0

def Clear(INDEX):
    OUTPUT_C = ""
    if POS - INDEX > 7:
        OUTPUT_C += "+x"
        INDEX += 10
        if POS - INDEX > 3:
            OUTPUT_C += "+v"
            INDEX += 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT_C += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT_C += "--"
                    INDEX -= 1
        elif POS - INDEX < -3:
            OUTPUT_C += "-v"
            INDEX -= 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT_C += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT_C += "--"
                    INDEX -= 1
        elif POS - INDEX > 0:
            for i in range(0, POS - INDEX):
                OUTPUT_C += "++"
                INDEX += 1
        elif POS - INDEX < 0:
            for i in range(0, abs(POS - INDEX)):
                OUTPUT_C += "--"
                INDEX -= 1
    elif POS - INDEX > 3:
        OUTPUT_C += "+v"
        INDEX += 5
        if POS - INDEX > 0:
            for i in range(0, POS - INDEX):
                OUTPUT_C += "++"
                INDEX += 1
        elif POS - INDEX < 0:
            for i in range(0, abs(POS - INDEX)):
                OUTPUT_C += "--"
                INDEX -= 1
    elif POS - INDEX > 0:
        for i in range(0, POS - INDEX):
            OUTPUT_C += "++"
            INDEX += 1
    
    return [OUTPUT_C, INDEX]


for token in USER_TOKENS:
    if token == "0":
        OUTPUT += "n(++--)"
    elif token == "1":
        OUTPUT += "n(++)"
    elif token == "2":
        OUTPUT += "n(++++)"
    elif token == "3":
        OUTPUT += "n(++++++)"
    elif token == "4":
        OUTPUT += "n(+v--)"
    elif token == "5":
        OUTPUT += "n(+v)"
    elif token == "6":
        OUTPUT += "n(+v++)"
    elif token == "7":
        OUTPUT += "n(+v++++)"
    elif token == "8":
        OUTPUT += "n(+v++++++)"
    elif token == "9":
        OUTPUT += "n(+v++++++++)"
    elif token == "_":
        OUTPUT += "s(++--)"
    elif token == ".":
        OUTPUT += "s(++)"
    elif token == "!":
        OUTPUT += "s(++++)"
    elif token == '?':
        OUTPUT += "s(++++++)"
    elif token == ',':
        OUTPUT += "s(+v--)"
    elif token == ":":
        OUTPUT += "s(+v)"
    elif token == "(":
        OUTPUT += "s(+v++)"
    elif token == ")":
        OUTPUT += "s(+v++++)"
    elif token == "@":
        OUTPUT += "s(+v++++++)"
    elif token == "#":
        OUTPUT += "s(+v++++++++)"
    elif token == "$":
        OUTPUT += "m(++--)"
    elif token == "+":
        OUTPUT += "m(++)"
    elif token == "-":
        OUTPUT += "m(++++)"
    elif token == '*':
        OUTPUT += "m(++++++)"
    elif token == '/':
        OUTPUT += "m(+v--)"
    elif token == "=":
        OUTPUT += "m(+v)"
    elif token == "%":
        OUTPUT += "m(+v++)"
    elif token == "^":
        OUTPUT += "m(+v++++)"
    elif token == "<":
        OUTPUT += "m(+v++++++)"
    elif token == ">":
        OUTPUT += "m(+v++++++++)"
    elif token == "\n":
        INDEX = 0
        OUTPUT += "\n"
    elif token in TOKENS:
        POS = TOKENS.index(token) + 1
        if (token == "a" or token == "e" or token == "j" or token == "t") and INDEX != 0:
            OUTPUT += "c"
            INDEX = 0
            clear_func = Clear(INDEX)
            OUTPUT += str(Clear(INDEX)[0])
            INDEX = clear_func[1]
        elif POS - INDEX > 0:
            if POS < POS - INDEX:
                OUTPUT += "c"
                INDEX = 0
                clear_func = Clear(INDEX)
                OUTPUT += str(Clear(INDEX)[0])
                INDEX = clear_func[1]
        elif POS - INDEX < 0:
            if 0 - POS > POS - INDEX:
                OUTPUT += "c"
                INDEX = 0
                clear_func = Clear(INDEX)
                OUTPUT += str(Clear(INDEX)[0])
                INDEX = clear_func[1]
        if POS - INDEX >= 20 or POS - INDEX > 17:
            OUTPUT += "+t"
            INDEX += 20
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 7:
            OUTPUT += "+x"
            INDEX += 10
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 3:
            OUTPUT += "+v"
            INDEX += 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 0:
            for i in range(0, POS - INDEX):
                OUTPUT += "++"
                INDEX += 1
        elif POS - INDEX < -7:
            OUTPUT += "-x"
            INDEX -= 10
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX < -3:
            OUTPUT += "-v"
            INDEX -= 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX < 0:
            for i in range(0, abs(POS - INDEX)):
                OUTPUT += "--"
                INDEX -= 1
        
        OUTPUT += "p"
        
    elif token in TOKENS_CAPS:
        POS = TOKENS_CAPS.index(token) + 1
        if (token == "A" or token == "E" or token == "J" or token == "T") and INDEX != 0:
            OUTPUT += "c"
            INDEX = 0
            clear_func = Clear(INDEX)
            OUTPUT += str(Clear(INDEX)[0])
            INDEX = clear_func[1]
        elif POS - INDEX > 0:
            if POS < POS - INDEX:
                OUTPUT += "c"
                INDEX = 0
                clear_func = Clear(INDEX)
                OUTPUT += str(Clear(INDEX)[0])
                INDEX = clear_func[1]
        elif POS - INDEX < 0:
            if 0 - POS > POS - INDEX:
                OUTPUT += "c"
                INDEX = 0
                clear_func = Clear(INDEX)
                OUTPUT += str(Clear(INDEX)[0])
                INDEX = clear_func[1]
        if POS - INDEX >= 20 or POS - INDEX > 17:
            OUTPUT += "+t"
            INDEX += 20
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 7:
            OUTPUT += "+x"
            INDEX += 10
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 3:
            OUTPUT += "+v"
            INDEX += 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX > 0:
            for i in range(0, POS - INDEX):
                OUTPUT += "++"
                INDEX += 1
        elif POS - INDEX < -7:
            OUTPUT += "-x"
            INDEX -= 10
            if POS - INDEX > 3:
                OUTPUT += "+v"
                INDEX += 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX < -3:
                OUTPUT += "-v"
                INDEX -= 5
                if POS - INDEX > 0:
                    for i in range(0, POS - INDEX):
                        OUTPUT += "++"
                        INDEX += 1
                elif POS - INDEX < 0:
                    for i in range(0, abs(POS - INDEX)):
                        OUTPUT += "--"
                        INDEX -= 1
            elif POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX < -3:
            OUTPUT += "-v"
            INDEX -= 5
            if POS - INDEX > 0:
                for i in range(0, POS - INDEX):
                    OUTPUT += "++"
                    INDEX += 1
            elif POS - INDEX < 0:
                for i in range(0, abs(POS - INDEX)):
                    OUTPUT += "--"
                    INDEX -= 1
        elif POS - INDEX < 0:
            for i in range(0, abs(POS - INDEX)):
                OUTPUT += "--"
                INDEX -= 1
        
        OUTPUT += "^p"
    
    elif token == " ":
        OUTPUT += "_"

print(OUTPUT)
