from gpa import calculate_old_GPA, convert_grade, get_class_grade
import pytest

def main():
    # Test the calculate_old_GPA function
    test_calculate_old_GPA()

    # Test the convert_grade function
    test_convert_grade()

    # Test the get_class_grade function
    test_get_class_grade()

def test_calculate_old_GPA():
    """
    Test the calculate_old_GPA function by calling it and
    comparing the values it returns to the expected values.
    """
    assert calculate_old_GPA(270, 80) == 3.375
    assert calculate_old_GPA(30, 10) == 3.0  
    assert calculate_old_GPA(120, 30) == 4.0
    assert calculate_old_GPA(12, 12) == 1.0

def test_convert_grade():
    """
    Test the convert_grade function by calling it and
    comparing the values it returns to the expected values.
    """
    assert convert_grade("A") == 4.0
    assert convert_grade("B-") == 2.7
    assert convert_grade("D-") == 0.7
    assert convert_grade("UW") == 0

def test_get_class_grade():
    """
    Test the get_class_grade function by calling it and
    comparing the values it returns to the expected values.
    """
    valid_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "UW"]
    skip_grades = ["P", "I", "W", "T", "NR"]

    assert "A" in valid_grades
    assert "B-" in valid_grades
    assert "C+" in valid_grades
    assert "D" in valid_grades
    assert "I" in skip_grades
    assert "NR" in skip_grades
    assert "W" in skip_grades
    assert "P" in skip_grades

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

