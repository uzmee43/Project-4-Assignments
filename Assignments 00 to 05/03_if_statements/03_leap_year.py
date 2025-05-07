def main() -> None:
    # Ask the user for a year
    year = int(input("Enter a year: "))

    # Check leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()
# The code checks if a given year is a leap year or not. A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The code uses the modulo operator (%) to check divisibility and prints the result accordingly.