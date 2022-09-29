def is_number(num1, num2) -> bool:
    return (isinstance(num1, float) or isinstance(num1, int)) and (isinstance(num2, float) or isinstance(num1, int))


class MathematicalFunctions:

    @staticmethod
    def sum_two_numbers(num1: float, num2: float) -> float:
        assert is_number(num1, num2)
        return num1 + num2

    @staticmethod
    def divide_two_numbers(num1: float, num2: float) -> float:
        assert is_number(num1, num2)
        assert num2 != 0
        return num1/num2
