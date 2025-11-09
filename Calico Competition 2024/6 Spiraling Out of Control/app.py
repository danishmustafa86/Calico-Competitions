def draw_spiral(n):
    size = 4 * n + 1  # Calculate the size of the grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]  # Initialize grid

    for layer in range(n):
        # Calculate the boundaries of the current layer
        start = 2 * layer
        end = size - 2 * (layer + 1)

        # Draw the top edge
        for col in range(start, end + 1):
            grid[start][col] = '@'

        # Draw the right edge
        for row in range(start + 1, end + 1):
            grid[row][end] = '@'

        # Draw the bottom edge
        for col in range(end - 1, start - 1, -1):
            grid[end][col] = '@'

        # Draw the left edge
        for row in range(end - 1, start, -1):
            grid[row][start] = '@'

    # Draw the final center point
    grid[2 * n][2 * n] = '@'

    # Convert grid to a string for output
    return '\n'.join(''.join(row) for row in grid)


def solve_spirals():
    T = int(input().strip())
    results = []

    for _ in range(T):
        n = int(input().strip())
        results.append(draw_spiral(n))

    # Print all results separated by a blank line
    print('\n\n'.join(results))


# Call the function to solve the problem
solve_spirals()
