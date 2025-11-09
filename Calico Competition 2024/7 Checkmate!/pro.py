# Directions for the king's possible moves (including diagonals)
KING_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def in_bounds(r, c, max_r, max_c):
    """Check if a position is within the chessboard's boundaries."""
    return 0 <= r < max_r and 0 <= c < max_c

def checkmate_spots(board, r, c):
    """Return the number of spots where a king is in checkmate."""
    
    # Initialize sets for rows, columns, and diagonals
    row_threatened = set()
    col_threatened = set()
    main_diag_threatened = set()
    anti_diag_threatened = set()
    
    # Find all queens and mark their attacking positions
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'Q':
                row_threatened.add(i)
                col_threatened.add(j)
                main_diag_threatened.add(i - j)
                anti_diag_threatened.add(i + j)

    # Now check for each empty spot if it's a checkmate
    checkmate_count = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == '-':
                # Check if the square is under threat
                if (i in row_threatened or 
                    j in col_threatened or 
                    (i - j) in main_diag_threatened or 
                    (i + j) in anti_diag_threatened):
                    
                    # Check if all adjacent squares are either under threat or out of bounds
                    is_checkmate = True
                    for dr, dc in KING_MOVES:
                        ni, nj = i + dr, j + dc
                        if in_bounds(ni, nj, r, c) and (ni, nj) not in threatened:
                            is_checkmate = False
                            break
                    if is_checkmate:
                        checkmate_count += 1
    return checkmate_count

def solve_spirals():
    T = int(input().strip())  # Read number of test cases
    results = []

    for _ in range(T):
        r, c = map(int, input().strip().split('x'))  # Read dimensions of the board
        board = []
        for i in range(r):
            board.append(input().strip())  # Read the board configuration

        results.append(str(checkmate_spots(board, r, c)))  # Find checkmate spots

        # Read the blank line separating test cases
        if _ < T - 1:
            input()

    print("\n".join(results))

# Call the function to solve the problem
solve_spirals()
