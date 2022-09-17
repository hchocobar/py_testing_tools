import pytest

from app.calculator import Calculator
from app.exceptions import MathematicalException


@pytest.fixture()
def calculator() -> Calculator:
    return Calculator()


@pytest.mark.parametrize('operation, result_expected', [((1, 2, 'add'), 3),
                                                        ((1, 2, 'subtraction'), -1),
                                                        ((1, 2, 'multiplication'), 2),
                                                        ((1, 2, 'division'), 0.5), ])
def test_calculate(operation, result_expected, calculator: Calculator):
    # calculator = Calculator()
    result = calculator.calculate(*operation)
    assert result == result_expected


def test_calculate_error_division_by_zero(calculator: Calculator):
    # calculator = Calculator()
    with pytest.raises(MathematicalException, match='The mathematical operation is not correct: .*'):
        calculator.calculate(0, 0, 'division')
