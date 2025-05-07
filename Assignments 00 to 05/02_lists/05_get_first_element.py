def get_first_element(lst: list) -> None:
    print("The first element in the list is:", lst[0])

def main() -> None:
    num_elements = int(input("How many elements in your list? "))
    user_list = []

    for i in range(num_elements):
        item = input(f"Enter element #{i + 1}: ")
        user_list.append(item)

    get_first_element(user_list)

if __name__ == '__main__':
    main()
# # Output: The program prompts the user to enter a number of elements and then prints the first element in the list.
# # The `get_first_element` function takes a list and prints its first element.