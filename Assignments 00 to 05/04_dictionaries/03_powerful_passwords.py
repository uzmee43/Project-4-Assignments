import hashlib

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 and returns the hex digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    """
    Returns True if the hash of password_to_check matches the stored hash
    for the given email in stored_logins. Otherwise returns False.
    """
    if email not in stored_logins:
        return False

    hashed_password = hash_password(password_to_check)
    return stored_logins[email] == hashed_password

def main():
    # Example stored logins with hashed passwords
    stored_logins = {
        "user@example.com": hash_password("mySecurePassword123"),
        "khane@web.com": hash_password("rabbi3333!"),
    }

    # Simulate a login attempt
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    if login(email_input, password_input, stored_logins):
        print("Login successful!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()
# This script demonstrates how to securely store and verify passwords using hashing.
# It uses the SHA-256 hashing algorithm to hash passwords before storing them in a dictionary.