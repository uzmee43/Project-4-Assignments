def print_multiple(message, repeats):
    """
    Prints the given message a specified number of times.
    """
    for _ in range(repeats):  # Loop 'repeats' number of times
        print(message)  # Print the message on a new line each time

def main():
    # Prompt the user for a message
    message = input("Please type a message: ")
    
    try:
        # Prompt the user for the number of repetitions
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)  # Call the helper function
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of repeats.")

# Run the main function
if __name__ == '__main__':
    main()
