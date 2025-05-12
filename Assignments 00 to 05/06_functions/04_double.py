def double(num):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    try:
        # Prompt the user for a number
        num = float(input("Enter a number: "))
        # Call the double function and print the result
        print("Double that is", double(num))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        

if __name__ == '__main__':
    main()
