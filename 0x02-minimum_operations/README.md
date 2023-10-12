Curriculum <br>
**Short Specializations** <br>

# 0x02. Minimum Operations

`Algorithm` `Python`

Minimum Operations
Description
This project is about finding the minimum number of operations required to transform one string into another. An operation can be one of the following:

Insert a character at any position of the string.
Delete a character from any position of the string.
Replace a character at any position of the string with another character.
For example, to transform “cat” into “dog”, we need three operations:

Replace “c” with “d”.
Replace “a” with “o”.
Replace “t” with “g”.
The minimum number of operations is also known as the edit distance or the Levenshtein distance between two strings.

Implementation
This project is implemented in Python 3. The main algorithm is based on dynamic programming, which uses a two-dimensional matrix to store the intermediate results. The algorithm has a time complexity of O(mn) and a space complexity of O(mn), where m and n are the lengths of the two strings.

The project consists of two files:

0-minoperations.py: This file contains the main function minOperations(n), which takes a string as input and returns the output. It also contains some helper functions to print the matrix and the operations.
0-main.py: This file contains some test cases to check the correctness and efficiency of the algorithm.
Usage
To run the project, you need to have Python 3 installed on your system. You can download it from [here].

To execute the main file, open a terminal and type:

python 0-minoperations.py

To run the test cases, type:

python 0-main.py

You can also modify the input strings in both files to test different scenarios.

References
This project is inspired by the following sources:

[Wikipedia: Levenshtein distance]
[GeeksforGeeks: Edit Distance | DP-5]
