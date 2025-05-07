def add_three_copies(lst: list, data) -> None:
    for _ in range(3):
        lst.append(data)

def main() -> None:
    message: str = input("Enter a message to copy: ")
    messages: list = []

    print("\nList before:", messages)
    add_three_copies(messages, message)
    print("List after:", messages)

if __name__ == '__main__':
    main()
# Output: The program prompts the user to enter a message and then creates a list with three copies of that message.
# The `add_three_copies` function takes a list and a data item, appending three copies of the data item to the list.