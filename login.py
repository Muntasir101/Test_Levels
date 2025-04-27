# login.py

def login(username, password):
    """
    Simulates a login process. Checks if the provided username and password match
    hardcoded credentials.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    # In a real application, you would look up the user in a database
    # and securely compare the hashed password.
    valid_username = "testuser"
    valid_password = "password123"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

