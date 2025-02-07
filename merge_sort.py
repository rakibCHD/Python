def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right) 

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result 

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

ascending_order = merge_sort(numbers[:])  # Sorting in ascending order
descending_order = merge_sort(numbers[:])[::-1]  # Sorting in descending order

print(f"List in ascending order: {ascending_order}")
print(f"List in descending order: {descending_order}")
 
  
   
