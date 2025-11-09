def solve(N: int, M: int, G: list) -> str:
    """
    Determines whether the given grid contains a triangle or rectangle.
    Returns "phineas" for a triangle or "ferb" for a rectangle.
    """
    # Find all the '#' in the grid to determine the bounds of the shape
    min_row, max_row, min_col, max_col = N, -1, M, -1
    for i in range(N):
        for j in range(M):
            if G[i][j] == '#':
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)
    
    # Calculate the dimensions of the bounding box
    height = max_row - min_row + 1
    width = max_col - min_col + 1

    # Check if it's a rectangle
    is_rectangle = True
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if G[i][j] != '#':
                is_rectangle = False
                break

    if is_rectangle:
        return "ferb"  # It's a rectangle

    # Check if it's a triangle
    # Scan the bounding box and ensure it's an isosceles right triangle
    # The triangle should only have '#' in its "isosceles triangle shape".
    for i in range(height):
        for j in range(i + 1):
            if G[min_row + i][min_col + j] != '#':
                return "phineas"  # It's a triangle

    return "phineas"

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
