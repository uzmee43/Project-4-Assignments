from typing import List

def double_elements(numbers: List[int]) -> List[int]:
    return [num * 2 for num in numbers]

def main() -> None:
    numbers: List[int] = [1, 2, 3, 4]
    doubled: List[int] = double_elements(numbers)
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled}")

if __name__ == '__main__':
    main()
