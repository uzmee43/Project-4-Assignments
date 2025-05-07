import math

def calculate_hypotenuse(ab: float, ac: float) -> float:
    return math.sqrt(ab ** 2 + ac ** 2)

def main() -> None:
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    
    bc: float = calculate_hypotenuse(ab, ac)
    
    print(f"\nThe length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()
# This program calculates the length of the hypotenuse of a right triangle using the Pythagorean theorem.
# It prompts the user for the lengths of the two other sides and then calculates and displays the length of the hypotenuse.