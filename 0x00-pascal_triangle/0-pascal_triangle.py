def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle

# Get the number of rows from the user
try:
    n = int(input("Enter the number of rows for Pascal's triangle: "))
    result = pascal_triangle(n)
    for row in result:
        print(row)
except ValueError:
    print("Please enter a valid integer for the number of rows.")
