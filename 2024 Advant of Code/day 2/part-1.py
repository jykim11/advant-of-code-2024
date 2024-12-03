def is_safe(levels):
    # Convert string numbers to integers
    nums = []
    for num in levels:
        num = int(num)
        nums.append(num)
    
    # Calculate differences between adjacent numbers
    differences = []
    for i in range(len(nums) - 1):
        difference = nums[i + 1] - nums[i]
        differences.append(difference)
    
    # Check if sequence is strictly increasing
    is_increasing = True  # Assume sequence is increasing until proven otherwise
    for diff in differences:
        if diff <= 0 or diff > 3:
            is_increasing = False
            break
    
    # Check if sequence is strictly decreasing
    is_decreasing = True  # Assume sequence is decreasing until proven otherwise
    for diff in differences:
        if diff >= 0 or diff < -3:
            is_decreasing = False
            break
    
    # Return True if either increasing or decreasing conditions are met
    return is_increasing or is_decreasing

# Read and process input file
safe_count = 0
file = open("input.txt", "r")

for line in file:
    report = line.strip().split()
    if is_safe(report):
        safe_count += 1

file.close()

print(f"Number of safe reports: {safe_count}")

# Time Complexity: O(n)
# Space Complexity: O(n)