import pytest as pytest

from mathematicalFunctions import MathematicalFunctions as mf


@pytest.fixture
def math_func():
    return mf()


def test_sum_two_numbers_parameters_error(math_func):
    with pytest.raises(AssertionError):
        math_func.sum_two_numbers("string", "string")


def test_sum_two_numbers_result(math_func):
    sum_numbers = math_func.sum_two_numbers(1.12, 2.26)
    assert sum_numbers == 3.38, "The sum is not correct."


def test_divide_two_numbers_result(math_func):
    division = math_func.divide_two_numbers(0.6, 1.2)
    assert division == 0.5, "The division is not correct."


def test_divide_two_numbers_division_by_zero_error(math_func):
    with pytest.raises(AssertionError):
        math_func.divide_two_numbers(1, 0)


def test_divide_two_numbers_parameters_error(math_func):
    with pytest.raises(AssertionError):
        math_func.divide_two_numbers("string", "string")

