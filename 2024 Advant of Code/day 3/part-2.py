def solve_part2(input_text):
    total = 0
    i = 0
    mul_enabled = True  # Start with mul instructions enabled
    
    while i < len(input_text):
        # Check for do() or don't() instructions
        if input_text[i:i+3] == "do(":
            mul_enabled = True
            i += 3  # Move past "do("
        elif input_text[i:i+6] == "don't(":
            mul_enabled = False
            i += 6  # Move past "don't("
        
        # Find start of potential mul instruction
        elif input_text[i:i+3] == "mul":
            # Check if next char is opening parenthesis
            if i + 3 < len(input_text) and input_text[i+3] == "(":
                start = i + 4  # Skip past "mul("
                end = start
                
                # Find the closing parenthesis
                while end < len(input_text) and input_text[end] != ")":
                    end += 1
                
                if end < len(input_text) and mul_enabled:
                    # Get the content between parentheses
                    numbers = input_text[start:end].split(",")
                    
                    # Validate format: exactly 2 numbers, each 1-3 digits
                    if (len(numbers) == 2 and 
                        numbers[0].isdigit() and numbers[1].isdigit() and
                        1 <= len(numbers[0]) <= 3 and 1 <= len(numbers[1]) <= 3):
                        total += int(numbers[0]) * int(numbers[1])
        i += 1
    
    return total

def main():
    file = open("input.txt", "r")
    input_text = file.read()
    file.close()
    print(solve_part2(input_text))

# Time complexity: O(n)
# Space complexity: O(1)

main()