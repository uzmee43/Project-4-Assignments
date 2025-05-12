def print_divisors(num):
    """
    Prints all divisors of the given number.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Iterate from 1 to num (inclusive)
        if num % i == 0:  # Check if i is a divisor
            print(i, end=" ")  # Print divisor on the same line
    print()  # Move to the next line after printing all divisors

def main():
    try:
        # Prompt the user for a number
        num = int(input("Enter a number: "))
        print_divisors(num)  # Call the helper function
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the main function
if __name__ == '__main__':
    main()
