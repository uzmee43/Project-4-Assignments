def main() -> None:
    # Create an empty phonebook dictionary
    phonebook = {}

    # Add some contacts
    phonebook["khan"] = "035-1234"
    phonebook["uzma"] = "035-5678"
    phonebook["ayisha"] = "035-8765"
    phonebook["nadia"] = "035-8798"

    # Print the phonebook
    print("Phonebook entries:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

    # Lookup a phone number
    name_to_lookup = input("\nEnter a name to look up: ")
    if name_to_lookup in phonebook:
        print(f"{name_to_lookup}'s number is {phonebook[name_to_lookup]}")
    else:
        print("That name is not in the phonebook.")

if __name__ == '__main__':
    main()
