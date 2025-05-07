MAX_LENGTH = 3

def shorten(lst: list) -> None:
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main() -> None:
    num_items = int(input("How many items in your list? "))
    items = []

    for i in range(num_items):
        item = input(f"Enter item #{i + 1}: ")
        items.append(item)

    print("\nOriginal list:", items)
    shorten(items)
    print("Final list:", items)

if __name__ == '__main__':
    main()
# # Output: The program prompts the user to enter a number of items and then shortens the list to a maximum length of 3.
# # The `shorten` function removes items from the end of the list until its length is less than or equal to 3.