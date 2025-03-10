# lib/not_none_functions.py

def get_value():
    # In your real code, this function will have some logic.
    # For demonstration, we're simply returning a non-None value.
    return "some_value"  # 


from lib.not_none_functions import get_value  # Import the function to test

def test_get_value_is_not_none():
    result = get_value()  # Call the function
    assert result is not None, "get_value() should not return None"  # Assert it is not None
