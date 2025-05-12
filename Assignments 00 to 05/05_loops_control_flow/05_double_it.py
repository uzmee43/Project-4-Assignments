# Prompt the user to enter a number
curr_value = int(input("Enter a number: "))

# Continue doubling the number while it's less than 100
while curr_value < 100:
    curr_value *= 2
    print(curr_value, end=" ")
