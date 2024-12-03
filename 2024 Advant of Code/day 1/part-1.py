def calculate_total_distance():
    left_nums = []
    right_nums = []
    total_distance = 0
    file = open("lists.txt", "r")

    for line in file:
        # strip the line of whitespace and split into two ints
        left, right = line.strip().split()
        left = int(left)
        right = int(right)
        left_nums.append(left)
        right_nums.append(right)
    
    # sort() is O(n log n)
    left_nums.sort()
    right_nums.sort()
    
    for i in range(len(left_nums)):
        total_distance += abs(left_nums[i] - right_nums[i])
    
    file.close()
    
    return total_distance

# Time complexity: O(n log n)
# Space complexity: O(n)

calculate_total_distance()