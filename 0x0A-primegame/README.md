Curriculum <br>
**Short Specializations** <br>

# 0x0A. Prime Game

`Algorithm` `Python`


## Introduction
The Prime Game project revolves around a strategic game played by two participants, Maria and Ben. The game is defined by selecting prime numbers from a set of consecutive integers starting from 1 up to and including a given integer 'n'. Subsequently, the chosen number and its multiples are systematically removed from the set. The player who cannot make a move loses the game. This intriguing process is repeated for a specified number of rounds 'x'. The challenge is to determine, with the assumption that Maria always goes first and both players play optimally, who emerges as the winner after each game.

## Problem Description
Implement the function `isWinner(x, nums)` with the following parameters:
- `x` is the number of rounds.
- `nums` is an array of integers representing 'n' for each round.

The primary goal of this function is to return the name of the player who won the most rounds. If the winner cannot be determined, the function should return `None`. It is important to note that 'n' and 'x' will not exceed 10,000, and the implementation should avoid importing any external packages.

## Function Prototype
```python
def isWinner(x, nums):
    # Your implementation here
```

## Example
```python
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins
```

## Constraints
- 1 <= x <= 10,000
- 1 <= n <= 10,000

## Approach
1. Implement the game logic to simulate Maria and Ben's moves.
2. Determine the winner for each round based on optimal play.
3. Keep track of the number of rounds won by each player.
4. Return the name of the player with the most wins or `None` if the winner cannot be determined.

## Usage
```python
isWinner(5, [2, 5, 1, 4, 3])
# Output: 'Ben'
```

## Execution
```bash
./main_0.py
# Output: Winner: Ben
```

This project explores the intricacies of game theory, algorithmic decision-making, and strategic gameplay within the context of prime numbers, providing an engaging challenge for both implementation and optimization.