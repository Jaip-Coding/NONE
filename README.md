# NONE
NONE is an esoteric programming language that can output text

## About
NONE is an esoteric programming language that can output text created by Jaip-Coding in 2023. Together with the included generator, it can also be used to encrypt and decrypt text to NONE format. The current version is 1.0

## Instructions
Download the repo and run "none.py" You can now enter NONE code into the terminal and execute it by pressing Enter.

## Syntax
NONE works with only 13 allowed characters: ```+ - c p n s ( ) _ ^ v x t```

### Index
NONE has an index that is set to zero at the beginning. It can be increased or decreased:

| NONE  | Description |
| ------------- | ------------- |
| ++  | Increases the index by 1 |
| --  | Decreases the index by 1 |
| +v  | Increases the index by 5 |
| -v  | Decreases the index by 5 |
| +x  | Increases the index by 10 |
| -x  | Decreases the index by 10 |
| +t  | Increases the index by 20 |
| -t  | Decreases the index by 20 |

v stands for 5, x for 10 and t for 20.

**Example**: ```+v--+t-x++++``` 

The index is first increased by 5, then decreased by 1, then increased by 20, decreased by 10 and finally increased by 1 twice. The final index would be 16.

### Print
A letter can be output with Print (p). It will output the letter that has the current value of the index as a position in the alphabet. So if the index is 1, the letter will be "a" or if the index is 26, the letter will be "z".

**Example**: ```+t-v--p```

The letter "n" will be output.

**Example 2**: ```++p+t+vp```

NONE can also output multiple letters. This program would output "az".
