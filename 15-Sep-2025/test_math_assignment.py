import math_assignment
import pytest

def test_multiply():
    assert math_assignment.multiply(5, 6)

def test_factorial():
    assert math_assignment.factorial(3) == 6

def test_prime_number():
    assert math_assignment.is_prime(3) == True

def test_area_Of_circle():
    assert math_assignment.area_of_circle(7) == 154
