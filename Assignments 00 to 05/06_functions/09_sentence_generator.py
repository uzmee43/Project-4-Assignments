def make_sentence(word, part_of_speech):
    """
    Prints a sentence using the given word and part of speech.
    """
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0, 1, or 2.")

def main():
    # Prompt the user for a word
    word = input("Please type a noun, verb, or adjective: ")

    try:
        # Prompt the user for the part of speech
        part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
        make_sentence(word, part_of_speech)  # Call the helper function
    except ValueError:
        print("Invalid input. Please enter an integer (0, 1, or 2) for the part of speech.")

# Run the main function
if __name__ == '__main__':
    main()
