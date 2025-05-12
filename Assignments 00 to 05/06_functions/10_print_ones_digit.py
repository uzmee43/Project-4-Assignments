def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = abs(num) % 10  # Get the absolute value's ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    try:
        # Prompt the user for a number
        num = int(input("Enter a number: "))
        print_ones_digit(num)  # Call the helper function
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the main function
if __name__ == '__main__':
    main()
