def main():
    r = int(input("Input number of rows to see Diamond pattern: "))

    # Upper part of the diamond
    for i in range(1, r + 1):
        for j in range(r, i, -1):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    # Lower part of the diamond
    for i in range(1, r):
        for j in range(i):
            print(" ", end="")
        for k in range((r - i) * 2 - 1):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
