import copy
import sys

# Screen dimensions
GRID_WIDTH = 7 # Grid
GRID_HEIGHT = 9 # Grid

# The 12 pentomino shapes
SHAPES = [
    [[0,0,1],
     [1,1,1],
     [0,1,0]],

    [[0,1,0],
     [1,1,1],
     [0,1,0]],

    [[0,0,1],
     [0,1,1],
     [1,1,0]],

    [[0,0,1,0],
     [1,1,1,1]],

    [[1,1,1],
     [1,0,0],
     [1,0,0]],

    [[1,0,0,0,],
     [1,1,1,1]],

    [[1,1,0],
     [0,1,0],
     [0,1,1]],

    [[1,1,1,1,1]],

    [[1,0,1],
     [1,1,1]],

    [[0,1,1],
     [1,1,1]],

    [[0,0,1,1],
     [1,1,1,0]],

    [[0,1,0],
     [0,1,0],
     [1,1,1]]
]

def rotate(shape):
    """Rotates a shape 90 degrees clockwise."""
    return [
        [shape[y][x] for y in range(len(shape))]
        for x in range(len(shape[0]) - 1, -1, -1)
    ]

def flip(shape):
    """Flips a shape horizontally."""
    return [row[::-1] for row in shape]

def get_all_orientations(shape):
    """Generates all unique rotations and flips for a shape."""
    orientations = []
    current_shape = shape
    # 2 for original and flipped
    for _ in range(2):
        # 4 rotations
        for _ in range(4):
            current_shape = rotate(current_shape)
            if current_shape not in orientations:
                orientations.append(current_shape)
        current_shape = flip(shape)
    return orientations

ALL_PIECES = [get_all_orientations(s) for s in SHAPES]

def can_place(board, piece, x, y):
    """Checks if a piece can be placed at (x, y) on the board."""
    # Add check for negative start coordinates to prevent wrap-around
    if x < 0 or y < 0:
        return False
    piece_height = len(piece)
    piece_width = len(piece[0])
    if x + piece_width > GRID_WIDTH or y + piece_height > GRID_HEIGHT:
        return False
    for r in range(piece_height):
        for c in range(piece_width):
            if piece[r][c] and board[y + r][x + c] != 0:
                return False
    return True

def place_piece(board, piece, x, y, piece_id):
    """Places a piece on the board."""
    piece_height = len(piece)
    piece_width = len(piece[0])
    for r in range(piece_height):
        for c in range(piece_width):
            if piece[r][c]:
                board[y + r][x + c] = piece_id

def find_most_constrained_empty_cell(board):
    """
    Finds the empty cell that is most constrained (has the most filled neighbors),
    which is a better heuristic for backtracking solvers.
    """
    max_neighbors = -1
    most_constrained_cell = None

    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            if board[r][c] == 0: # It's an empty cell
                if most_constrained_cell is None:
                    most_constrained_cell = (r, c) # Pick the first one as a default

                neighbors = 0
                # Check 4 directions for non-empty cells (value != 0) or out of bounds
                if r == 0 or board[r - 1][c] != 0:
                    neighbors += 1
                if r == GRID_HEIGHT - 1 or board[r + 1][c] != 0:
                    neighbors += 1
                if c == 0 or board[r][c - 1] != 0:
                    neighbors += 1
                if c == GRID_WIDTH - 1 or board[r][c + 1] != 0:
                    neighbors += 1

                if neighbors > max_neighbors:
                    max_neighbors = neighbors
                    most_constrained_cell = (r, c)
                    # A cell with 4 neighbors is completely enclosed, must be the next one
                    if max_neighbors == 4:
                        return most_constrained_cell

    if most_constrained_cell:
        return most_constrained_cell
    return None, None # Board is full


def solve(board, pieces_to_place, piece_id=1):
    """Backtracking solver using a 'most constrained cell' heuristic."""
    # Find the most strategic empty cell to try and fill
    row, col = find_most_constrained_empty_cell(board)
    if row is None:
        return board # Solution found

    tried_placements = set() # Avoids redundant checks for the same piece placement

    # Try to place each of the remaining pieces
    for i, piece_orientations in enumerate(pieces_to_place):
        for orientation in piece_orientations:
            piece_h = len(orientation)
            piece_w = len(orientation[0])
            # Try to place the piece so that one of its blocks covers (row, col)
            for r_piece in range(piece_h):
                for c_piece in range(piece_w):
                    if orientation[r_piece][c_piece]:
                        # This block of the piece will cover the board's (row, col)
                        board_r_start = row - r_piece
                        board_c_start = col - c_piece

                        # Key to identify this exact placement attempt
                        orientation_tuple = tuple(map(tuple, orientation))
                        placement_key = (board_r_start, board_c_start, i, orientation_tuple)

                        if placement_key in tried_placements:
                            continue

                        if can_place(board, orientation, board_c_start, board_r_start):
                            tried_placements.add(placement_key)
                            new_board = copy.deepcopy(board)
                            place_piece(new_board, orientation, board_c_start, board_r_start, piece_id)

                            remaining_pieces = pieces_to_place[:i] + pieces_to_place[i+1:]
                            solution = solve(new_board, remaining_pieces, piece_id + 1)
                            if solution:
                                return solution
    return None # No solution found from this state

def print_board(board):
    """Prints the board."""
    if board is None:
        print("No solution found.")
        return
    # For better visual distinction of pieces
    piece_chars = "▣★○●◎◇◆□■▽▼♣♡"
    for row in board:
        print(" ".join(piece_chars[val] if val != -1 else 'X' for val in row))


if __name__ == "__main__":
    # Initialize board
    board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    blocked_cells = []

    print("Enter the coordinates of the 3 blocked cells (row col), one per line.")
    print(f"Row should be between 0 and {GRID_HEIGHT - 1}, col between 0 and {GRID_WIDTH - 1}.")
    print("For example, to select first row, first column (top-left corner) enter '0 0'")

    # Handle non-interactive input
    input_lines = []
    if not sys.stdin.isatty():
        raw_input = sys.stdin.read().strip()
        # Shells might pass literal '\\n' instead of newlines, so we replace it with a real newline
        input_lines = raw_input.replace('\\n', '\n').split('\n')
        input_lines = [line for line in input_lines if line] # remove empty lines
        if len(input_lines) < 3:
            print("\nNot enough coordinates provided for non-interactive mode.")
            sys.exit(1)

    for i in range(3):
        while True:
            try:
                if not sys.stdin.isatty():
                    # Use the pre-read lines
                    inp = input_lines[i]
                    print(f"Blocked cell {i+1}: {inp.strip()}")
                else:
                    # Get input interactively
                    inp = input(f"Blocked cell {i+1}: ")

                r, c = map(int, inp.split())
                if 0 <= r < GRID_HEIGHT and 0 <= c < GRID_WIDTH:
                    if (r, c) not in blocked_cells:
                        board[r][c] = -1 # Mark as blocked
                        blocked_cells.append((r,c))
                        break # Success, move to next cell
                    else:
                        print("Cell already blocked. Try another.")
                else:
                    print("Invalid coordinates. Please stay within the grid.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers separated by a space.")
                if not sys.stdin.isatty():
                    sys.exit(1) # Exit on bad data in non-interactive mode
                # In interactive mode, just loop and ask again
            except IndexError:
                print("\nNot enough coordinates provided for non-interactive mode.")
                sys.exit(1)

    print("\nStarting solver...")
    solution = solve(board, ALL_PIECES)
    print("\nSolution:")
    print_board(solution)

