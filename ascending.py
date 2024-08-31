def sort_ascending(numbers):
    return sorted(numbers)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
ascending_order = sort_ascending(numbers)
print(f"List in ascending order: {ascending_order}")  
 
   
  
  
 