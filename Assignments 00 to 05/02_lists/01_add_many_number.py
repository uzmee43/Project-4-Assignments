from typing import List

def sum_numbers(numbers: List[float]) -> float:
    return sum(numbers)

def main() -> None:
    # Example list
    my_list: List[float] = [1.5, 2, 3.5, 4]
    total: float = sum_numbers(my_list)
    print(f"The sum is: {total}")

if __name__ == '__main__':
    main()
# Output: The sum is: 11.0
# The code defines a function `sum_numbers` that takes a list of numbers and returns their sum.