INCHES_PER_FOOT: int = 12  # Constant: 12 inches in a foot

def convert_feet_to_inches(feet: float) -> float:
    return feet * INCHES_PER_FOOT

def main() -> None:
    feet_input: float = float(input("Enter length in feet: "))
    inches: float = convert_feet_to_inches(feet_input)
    
    print(f"{feet_input} foot{'s' if feet_input != 1 else ''} is equal to {inches} inches.")

if __name__ == '__main__':
    main()
# This program converts feet to inches.
# It prompts the user for a length in feet and then calculates and displays the equivalent length in inches.