def pascal_triangle(n):
    # Check if n is less than or equal to 0, and return an empty list in that case
    if n <= 0:
        return []

    # Initialize the triangle with the first row, which is always [1]
    triangle = [[1]]

    # Loop to generate the subsequent rows
    for _ in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]

        # Initialize a new row with 1 as its first element
        new_row = [1]

        # Loop to calculate the elements in the new row
        for i in range(1, len(prev_row)):
            # Calculate each element by summing two elements from the previous row
            new_row.append(prev_row[i - 1] + prev_row[i])

        # Add 1 as the last element of the new row
        new_row.append(1)

        # Append the new row to the triangle
        triangle.append(new_row)

    # Return the generated Pascal's triangle
    return triangle

def print_triangle(triangle):
    # Helper function to print the triangle
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # When the script is run, it prints Pascal's triangle up to the 5th row
    print_triangle(pascal_triangle(5))
