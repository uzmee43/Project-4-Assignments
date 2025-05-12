def count_even(lst):
    """
    Returns the number of even numbers in the list.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = sum(1 for num in lst if num % 2 == 0)  # Count even numbers using a generator
    return count  # Return the count instead of printing it

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Initialize an empty list
    while True:
        user_input = input("Enter an integer or press enter to stop: ")  # Prompt the user
        if user_input == "":  # Stop if input is empty
            break
        try:
            lst.append(int(user_input))  # Convert to integer and add to list
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Handle non-integer input
    return lst

def main():
    lst = get_list_of_ints()  # Get the list of integers from the user
    even_count = count_even(lst)  # Count the even numbers
    print(f"Number of even numbers: {even_count}")  # Print the result

# Ensure the script runs only when executed directly
if __name__ == '__main__':
    main()

