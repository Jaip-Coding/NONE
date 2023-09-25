# NONE
NONE is an esoteric programming language that can output letters, numbers and special characters.

## About
NONE is an esoteric programming language that can output text created by Jaip-Coding in 2023. Together with the included generator, it can also be used to encrypt and decrypt text to NONE format. The current version is 1.0

## Instructions
Download the repo and run "none.py" You can now enter NONE code into the terminal and execute it by pressing Enter.

## Syntax
NONE works with only 14 allowed characters: ```+ - c p n s m ( ) _ ^ v x t```

### Index
NONE has an index that is set to zero at the beginning. It can be increased or decreased:

| NONE | Description |
| ------------- | ------------- |
| ++ | Increases the index by 1 |
| -- | Decreases the index by 1 |
| +v | Increases the index by 5 |
| -v | Decreases the index by 5 |
| +x | Increases the index by 10 |
| -x | Decreases the index by 10 |
| +t | Increases the index by 20 |
| -t | Decreases the index by 20 |

v stands for 5, x for 10 and t for 20.

**Example**: ```+v--+t-x++++``` 

The index is first increased by 5, then decreased by 1, then increased by 20, decreased by 10 and finally increased by 1 twice. The final index would be 16.

### Print
A letter can be output with Print (p). It will output the letter that has the current value of the index as a position in the alphabet. So if the index is 1, the letter will be "a" or if the index is 26, the letter will be "z".

**Example**: ```+t-v--p```

The letter "n" will be output.

**Example 2**: ```++p+t+vp```

NONE can also output multiple letters. This program would output "az".

### Clear, Whitespace and capitalized

**Clear (c)**

With Clear (c), the index can be reset to 0

**Whitespace (_)**

You can make Whitespace between the letters with "_"

**Capitalize letters (^)**

You can capitalize letters by putting a "^" before Print (p)

### Numbers

You can write numbers with n() and put a number as a NONE index between the parentheses. +x and +t are not allowed. It will be output immediately even without print

**Example**: ```n(+v++)```

The output will be "6"

### Special characters

You can write special characters with s() and put a number as a NONE index between the parentheses as with numbers. +x and +t are not allowed. It will be output immediately even without print.

| NONE | character |
| ------------- | ------------- |
| s(++--) | _ |
| s(++) | . |
| s(++++) | ! |
| s(++++++) | ? |
| s(+v--) | , |
| s(+v) | : |
| s(+v++) | ( |
| s(+v++++) | ) |
| s(+v++++++) | @ |
| s(+v++++++++) | # |

### Mathematical characters

You can write mathematical characters with m() and put a number as a NONE index between the parentheses as with numbers and special characters. +x and +t are not allowed. It will be output immediately even without print.

| NONE | character |
| ------------- | ------------- |
| m(++--) | $ |
| m(++) | + |
| m(++++) | - |
| m(++++++) | * |
| m(+v--) | / |
| m(+v) | : |
| m(+v++) | ( |
| m(+v++++) | ) |
| m(+v++++++) | < |
| m(+v++++++++) | > |
