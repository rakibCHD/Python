def main():
    n = int(input("Enter a number to calculate factorial: "))
    f = 1

    for i in range(1, n + 1):
        f *= i

    print(f"Factorial of {n} is: {f}")

if __name__ == "__main__":
    main()
