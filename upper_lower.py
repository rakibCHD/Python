string = input("Enter a string: ")
choice = input("Choose 'upper'= u or 'lower'= l : ").strip().lower()

if choice == 'u' or 'U':
    result = string.upper()
elif choice == 'l' or 'L':
    result = string.lower()
else:
    result = "Invalid choice"

print(result)
