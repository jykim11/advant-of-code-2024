DIRECTIONS = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1), # left
        (-1, 0), # up
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]

ROW = 0
COLUMN = 0

def is_mas(i, j, di, dj, grid):
    word = "MAS"
    # Check forwards
    forwards = True
    for index, char in enumerate(word):
        newRow = i + index * di
        newColumn = j + index * dj
        if not (0 <= newRow < ROW and 0 <= newColumn < COLUMN) or grid[newRow][newColumn] != char:
            forwards = False
            break
    
    # Check backwards
    backwards = True
    reversedWord = word[::-1]  # "SAM"
    for index, char in enumerate(reversedWord):
        newRow = i + index * di
        newColumn = j + index * dj
        if not (0 <= newRow < ROW and 0 <= newColumn < COLUMN) or grid[newRow][newColumn] != char:
            backwards = False
            break
            
    return forwards or backwards

def count_mas(grid):
    count = 0
    for i in range(ROW - 2):  # Account for out-of-bounds
        for j in range(COLUMN - 2):  # Account for out-of-bounds
            # Check for X-MAS pattern
            # before "or" is down-right and down-left diagonals (\, /)
            # after "or" is up-right and up-left diagonals (/, \)
            if (is_mas(i, j, 1, 1, grid) and is_mas(i + 2, j, -1, 1, grid)) or \
               (is_mas(i, j + 2, 1, -1, grid) and is_mas(i + 2, j + 2, -1, -1, grid)):
                count += 1
    return count

def main():
    # Read input from file
    file = open("2024 Advant of Code/day 4/input.txt", "r")
    grid = [line.strip() for line in file.readlines()]

    global ROW, COLUMN
    ROW = len(grid)
    COLUMN = len(grid[0])

    result = count_mas(grid)
    print(result)

if __name__ == "__main__":
    main()
  

# Time Complexity: O(n * m)