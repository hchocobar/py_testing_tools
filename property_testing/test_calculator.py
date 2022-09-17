from hypothesis import given, strategies as st

from app.calculator import Calculator
from app.exceptions import OperationDoesntExist, MathematicalException

INVERSE_OPERATION = {'add': 'subtraction',
                     'subtraction': 'add',
                     'multiplication': 'division',
                     'division': 'multiplication'}


@given(op1=st.floats(width=16),
       op2=st.floats(width=16),
       operation=st.sampled_from(['add', 'subtraction', 'multiplication', 'division']))
def test_calculate_is_working(op1: int, op2: int, operation: str):
    calculator = Calculator()

    try:
        result = calculator.calculate(op1, op2, operation)
        assert op1 == calculator.calculate(result, op2, INVERSE_OPERATION[operation])
    except (MathematicalException, OperationDoesntExist):
        return
