C: int = 299_792_458  # The speed of light in m/s

def calculate_energy(mass_in_kg: float) -> float:
    return mass_in_kg * (C ** 2)

def main() -> None:
    while True:
        user_input: str = input("Enter kilos of mass (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting program.")
            break

        try:
            mass_in_kg: float = float(user_input)
            energy_in_joules: float = calculate_energy(mass_in_kg)

            print("e = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(str(energy_in_joules) + " joules of energy!\n")

        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to quit.\n")

if __name__ == '__main__':
    main()
