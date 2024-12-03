# Function from Part 1
def is_safe(levels):
    # Calculate differences between adjacent numbers
    differences = []
    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]
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


"""
This function checks if a sequence is safe by removing one number at a time and checking if the remaining sequence is safe
"""
def is_safe_with_dampener(levels):
    
    # First check if it's safe without removing any number
    if is_safe(levels):
        return True
    
    # Try removing each number one at a time
    for i in range(len(levels)):
        # Create new sequence without current number
        test_sequence = levels[:i] + levels[i+1:]

        # Check if this sequence is safe
        if is_safe(test_sequence):
            return True
            
    return False


def main():
    safe_count = 0
    file = open("2024 Advant of Code/day 2/input.txt", "r")
    for line in file: 
        report = [int(num) for num in line.strip().split()] # Convert string numbers to integers
        if is_safe_with_dampener(report):
            safe_count += 1

    print(f"Number of safe reports with Problem Dampener: {safe_count}")

main()