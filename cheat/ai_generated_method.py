# flake8: noqa
import re


def validate_last_name(last_name: str) -> bool:
    # Check if the length is less than 3 characters
    if len(last_name) < 3:
        return False
    
    # Check if it starts or ends with a hyphen
    if last_name.startswith('-') or last_name.endswith('-'):
        return False
    
    # Check for consecutive hyphens
    if '--' in last_name:
        return False
    
    # Check for invalid characters using regex
    # Valid characters are: upper case alphabetic, lower case alphabetic, apostrophe, hyphen
    if not re.match("^[a-zA-Z'-]+$", last_name):
        return False

    return True