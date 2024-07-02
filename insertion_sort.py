def insertion_sort_ascending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

ascending_order = insertion_sort_ascending(numbers[:])
descending_order = insertion_sort_descending(numbers[:])

print(f"List in ascending order: {ascending_order}")
print(f"List in descending order: {descending_order}")
