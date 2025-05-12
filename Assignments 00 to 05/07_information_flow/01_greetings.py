def greet(name):
    """
    Prints a greeting message with the given name.
    """
    print(f"Greetings {name}!")

def main():
    # Prompt the user for their name
    name = input("What's your name? ")
    greet(name)  # Call the helper function to greet the user

# Run the main function
if __name__ == '__main__':
    main()
