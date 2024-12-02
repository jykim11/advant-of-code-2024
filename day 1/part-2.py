def calculate_similarity_score():
    right_counts = {}
    total_score = 0
    file = open("lists.txt", "r")

    left_nums = []

    for line in file:
        left, right = line.strip().split()
        left = int(left)
        right = int(right)
        left_nums.append(left)
        right_counts[right] = right_counts.get(right, 0) + 1
    
    # For each left number:
    # 1. get(left, 0) looks up how many times this number appears in right list
    # 2. multiply left number by its count in right list
    # 3. add result to total_score
    for left in left_nums:
        total_score += left * right_counts.get(left, 0)
    
    return total_score

# Time complexity: O(n)
# Space complexity: O(n)
calculate_similarity_score()
