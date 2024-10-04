def main():
    r = int(input("Input number of rows to see Star: "))

    for i in range(1, r + 1):
        for j in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
 
