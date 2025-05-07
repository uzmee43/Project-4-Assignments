def main() -> None:
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    if divisor == 0:
        print("Division by zero is not allowed.")
        return

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
# # This program performs integer division and calculates the remainder.
# # It prompts the user for a dividend and divisor, performs the division, and displays the quotient and remainder.