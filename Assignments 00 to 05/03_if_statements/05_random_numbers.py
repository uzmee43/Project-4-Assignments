import random

def main() -> None:
    for _ in range(10):
        value = random.randint(1, 100)
        print(value, end=' ')
    print()  # Print newline at the end

if __name__ == '__main__':
    main()
# # The code generates and prints 10 random integers between 1 and 100. It uses the `random.randint` function to generate each random number and prints them in a single line, separated by spaces.
# # The `end=' '` argument in the print function ensures that the numbers are printed on the same line with a space between them. Finally, it prints a newline character after all numbers are printed.