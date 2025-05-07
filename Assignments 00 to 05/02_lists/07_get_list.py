def main() -> None:
    values = []

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)

    print("Here's the list:", values)

if __name__ == '__main__':
    main()
# # Output: The program prompts the user to enter values until an empty string is entered, then prints the list of values.
# # The `main` function initializes an empty list and appends user inputs to it until an empty string is entered.