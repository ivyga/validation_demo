from validator import validate_last_name

'''
Story AC:

Reject last names where
1. Input is less than 3 characters
2. Input starts with a hyphen
3. Input ends with a hyphen
4. Input contains consecutive hyphens
5. Input contains characters OTHER than
    Upper case alphbetic
    Lower case alphabetic
    Apostrophe 
    Hyphen
'''


# AC #1
def test_validate_last_name__too_short__returns_false():
    # arrange
    invalid_input = "Iv"

    # act
    actual = validate_last_name(invalid_input)

    # assert
    assert actual is False
