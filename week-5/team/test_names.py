from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Elizabeth", "Rodriguez") == "Rodriguez; Elizabeth"
    assert make_full_name("Amelia-Rose", "Allen") == "Allen; Amelia-Rose"

def test_extract_family():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Rodriguez; Elizabeth") == "Rodriguez"
    assert extract_family_name("Allen; Amelia-Rose") == "Allen"

def test_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Rodriguez; Elizabeth") == "Elizabeth"
    assert extract_given_name("Allen; Amelia-Rose") == "Amelia-Rose"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])