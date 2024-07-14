def main():
    a = int(input("Enter integer quantity to check prime/not prime: "))
    print("Input integers:")
    
    arr = [int(input()) for _ in range(a)]
    
    for number in arr:
        is_prime = True

        if number == 0 or number == 1:
            is_prime = False
        else:
            for i in range(2, number // 2 + 1):
                if number % i == 0:
                    is_prime = False
                    break

        print(f"{number} is {'a prime number' if is_prime else 'not a prime number'}")

if __name__ == "__main__":
    main()
