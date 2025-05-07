def get_last_element(lst: list) -> None:
    print("The last element in the list is:", lst[-1])

def main() -> None:
    num_elements = int(input("How many elements in your list? "))
    user_list = []

    for i in range(num_elements):
        item = input(f"Enter element #{i + 1}: ")
        user_list.append(item)

    get_last_element(user_list)

if __name__ == '__main__':
    main()
