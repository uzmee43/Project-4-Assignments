SENTENCE_START: str = "Code in Place is fun. I learned to program and used Python to make my"

def main() -> None:
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()
# # This program generates a mad lib by prompting the user for an adjective, noun, and verb.
# # It then constructs a sentence using these words and displays it.