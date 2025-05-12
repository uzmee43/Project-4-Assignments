import random

# Likelihood of being done (between 0 and 1)
DONE_LIKELIHOOD = 0.3

def done():
    """Simulate whether we're done with a certain likelihood."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for num in range(1, 11):
        if done():
            return
        print(num, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

main()


