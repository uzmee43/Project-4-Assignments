MINIMUM_HEIGHT : int = 50 

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':

    main()
# The code checks if a person is tall enough to ride a ride based on a minimum height requirement. If the person's height is greater than or equal to the minimum height, they are allowed to ride; otherwise, they are not.
# The code uses a constant for the minimum height and compares it with the user's input height. It prints a message based on the comparison result.