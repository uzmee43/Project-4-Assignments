import random
# This program simulates rolling two dice and prints the result.

NUM_SIDES = 6
def roll_dice():

    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    totel = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {totel}")
def main():
    die1 = 10
    print(f"Die in main() start as {die1}")
    for i in range(3):
        roll_dice()
        print(f"Die in main() end as {die1}")
if __name__ == "__main__":
        main()