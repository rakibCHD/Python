def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_descending(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

ascending_order = bubble_sort_ascending(numbers[:])
descending_order = bubble_sort_descending(numbers[:])  

print(f"List in ascending order: {ascending_order}")
print(f"List in descending order: {descending_order}")
 
      
 