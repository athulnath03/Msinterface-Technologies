def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    
    if num in [grid[r][col] for r in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    
    return True

def solve_sudoku(grid):
    empty_pos = find_empty(grid)
    if not empty_pos:
        return True  
    
    row, col = empty_pos
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  
    
    return False

def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def main():
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("Unsolved Sudoku Grid:")
    print_grid(sudoku_grid)
    
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
