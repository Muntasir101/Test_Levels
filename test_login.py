
from login import login  # Import the login function from your login.py file

def test_successful_login():
    """Test with correct username and password."""
    assert login("testuser", "password123") is True

def test_incorrect_password():
    """Test with correct username and incorrect password."""
    assert login("testuser", "wrongpassword") is False

def test_incorrect_username():
    """Test with incorrect username and correct password."""
    assert login("wronguser", "password123") is False

def test_incorrect_username_and_password():
    """Test with incorrect username and incorrect password."""
    assert login("wronguser", "wrongpassword") is False

def test_empty_username():
    """Test with empty username and correct password."""
    assert login("", "password123") is False

def test_empty_password():
    """Test with correct username and empty password."""
    assert login("testuser", "") is False

def test_empty_username_and_password():
    """Test with empty username and empty password."""
    assert login("", "") is False

# pytest allows grouping tests in classes, but it's not mandatory
# class TestLoginScenarios:
#     def test_successful_login_in_class(self):
#         assert login("testuser", "password123") is True
#     # ... add other tests here