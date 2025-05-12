def main():
    for i in range(10, 20):  # Loop through the numbers from 10 to 19
        if is_odd(i):
            print(f"{i} odd")  # Print the number followed by 'odd'
        else:
            print(f"{i} even")  # Print the number followed by 'even'

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    remainder = value % 2  # 0 if divisible by 2, 1 if not
    return remainder == 1  # Return true if the remainder is 1

if __name__ == '__main__':
    main()
