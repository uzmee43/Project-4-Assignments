def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address


def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
     main()
# This code defines a function `get_user_info` that prompts the user for their first name, last name, and email address.
# It then returns these values as a tuple. The `main` function calls `get_user_info` and prints the received user data.