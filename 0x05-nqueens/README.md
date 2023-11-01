Curriculum <br>
**Short Specializations** <br>

# 0x05. N Queens

`Algorithm` `Python`

# N Queens Problem Solver

The **N Queens Problem Solver** is a Python program designed to solve the classic chessboard puzzle. The challenge is to place N non-attacking queens on an N×N chessboard. This program efficiently finds and displays all possible solutions for the N Queens problem.

## Usage

```bash
python 0-nqueens.py N
```

- **N**: An integer representing the size of the chessboard. It must be greater or equal to 4.

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/alx-interview.git
   cd alx-interview/0x05-nqueens
   ```

2. **Run the Program:**
   ```bash
   python 0-nqueens.py N
   ```

## Input Constraints

- **N must be an integer** greater or equal to 4.
- If the user provides the wrong number of arguments, the program will exit with status 1 and print: `Usage: nqueens N`.
- If N is not an integer, the program will exit with status 1 and print: `N must be a number`.
- If N is smaller than 4, the program will exit with status 1 and print: `N must be at least 4`.

## Output

The program will print every possible solution to the N Queens problem. Each solution is represented as a list of queen positions, where each position is a pair `[row, column]`.

## Example

```bash
$ python 0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ python 0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Notes

- The solutions are printed one per line.
- The order of the solutions may vary.

---

**Note:** This program solves the N Queens problem using backtracking, a classic algorithmic approach to find solutions efficiently. The code ensures that no two queens threaten each other, fulfilling the conditions of the problem statement.