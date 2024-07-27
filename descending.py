def sort_descending(numbers):
    return sorted(numbers, reverse=True)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
descending_order = sort_descending(numbers)
print(f"List in descending order: {descending_order}")
 
   
  
