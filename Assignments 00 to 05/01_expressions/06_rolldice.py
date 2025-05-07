import random

def roll_die() -> int:
    return random.randint(1, 6)

def main() -> None:
    die1: int = roll_die()
    die2: int = roll_die()
    total: int = die1 + die2

    print(f"You rolled a {die1} and a {die2}.")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()
# # This program simulates rolling two dice and prints the result.
# # It uses the random module to generate random numbers between 1 and 6 (inclusive) for each die.