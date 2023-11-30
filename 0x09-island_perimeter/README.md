Curriculum <br>
**Short Specializations** <br>

# Island Perimeter (0x09)

## Overview
This project focuses on solving the "Island Perimeter" problem using Python. The algorithm is designed to calculate the perimeter of an island represented by a grid, where cells with a value of 1 denote land, and cells with a value of 0 denote water. The goal is to determine the total perimeter of the island based on its layout in the grid.

## Problem Statement
Given a 2D grid representing an island, where 1 represents land and 0 represents water, calculate the total perimeter of the island. The island is surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). The perimeter is the number of edges between land and water.

## Algorithm
The algorithm employs a straightforward approach to traverse the grid and calculate the perimeter. For each land cell (1) encountered, the algorithm checks its surrounding cells to determine the number of water cells (0) neighboring the land cell. The perimeter contribution from that land cell is then calculated based on the count of neighboring water cells.

## Implementation
The Python script (`island_perimeter.py`) contains the algorithm implementation, along with explanatory comments to guide through the code. The script can be executed standalone or integrated into larger projects dealing with grid-based problems.

## How to Use
1. Clone the repository: `git clone https://github.com/your-username/island-perimeter.git`
2. Navigate to the project directory: `cd island-perimeter`
3. Open and review the `island_perimeter.py` file for the algorithm implementation.
4. Run the script: `python island_perimeter.py`
5. Input the island grid as prompted by the script.

## Example
```python
# Example Input
3
3
0 1 0
0 1 0
0 0 0

# Example Output
8
```

## Dependencies
- Python

## Notes
- The algorithm assumes a valid island grid as input.

## Contributors
- [Your Name]
- [Contributor 1]
- [Contributor 2]

