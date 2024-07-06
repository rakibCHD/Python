def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

ascending_order = quick_sort(numbers[:])  # Sorting in ascending order
descending_order = quick_sort(numbers[:])[::-1]  # Sorting in descending order

print(f"List in ascending order: {ascending_order}")
print(f"List in descending order: {descending_order}") 
