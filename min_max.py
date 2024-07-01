def find_min_max(numbers):
    if len(numbers) == 0:
        return None, None
    
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    return min_number, max_number

# Prompt the user to enter numbers
user_input = input("Enter numbers separated by spaces: ")

# Convert the user input to a list of integers
numbers = list(map(int, user_input.split()))

# Find the minimum and maximum numbers in the list
min_number, max_number = find_min_max(numbers)

# Print the results
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
