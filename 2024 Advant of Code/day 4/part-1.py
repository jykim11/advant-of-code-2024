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

def is_xmas_at(i, j, di, dj, grid):
    word = "XMAS"
    for index, char in enumerate(word):
        newRow = i + index * di
        newColumn = j + index * dj
        if not (0 <= newRow < ROW and 0 <= newColumn < COLUMN) or grid[newRow][newColumn] != char:
            return False
    return True

def count_xmas(grid):    
    count = 0
    for i in range(ROW):
        for j in range(COLUMN):
            for di, dj in DIRECTIONS:
                if is_xmas_at(i, j, di, dj, grid):
                    count += 1
    return count

def main():
    # Read input from file
    file = open("2024 Advant of Code/day 4/input.txt", "r")
    grid = [line.strip() for line in file.readlines()]

    global ROW, COLUMN
    ROW = len(grid)
    COLUMN = len(grid[0])

    result = count_xmas(grid)
    print(result)

if __name__ == "__main__":
    main()

# Time Complexity: O(n * m)