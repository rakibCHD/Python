def main():
    print("\nInput two numbers to find GCD:")
    n1 = int(input("    "))
    n2 = int(input("    "))

    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            g = i

    print("Greatest Common Divisor (GCD) is:", g)

if __name__ == "__main__":
    main()
   