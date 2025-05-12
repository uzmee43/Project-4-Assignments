def subtract_seven(num):
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7

def main():
    try:
        # Prompt the user for a number
        num = int(input("Enter a number: "))
        # Call the helper function and print the result
        result = subtract_seven(num)
        print(f"Result after subtracting 7: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the main function
if __name__ == '__main__':
    main()
# This code defines a function `subtract_seven` that subtracts 7 from a given number.