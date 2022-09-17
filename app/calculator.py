from app.exceptions import OperationDoesntExist, MathematicalException


class Calculator:
    OPERATIONS = {
        'add': '+',
        'subtraction': '-',
        'multiplication': '*',
        'division': '/'
    }

    def get_expression(self, num1: float, num2: float, operation: str) -> str:
        try:
            opr: str = self.OPERATIONS[operation]
        except KeyError:
            raise OperationDoesntExist('The operation cannot be found')

        expression = f'{num1}{opr}{num2}'
        return expression

    def calculate(self, num1: float, num2: float, operation: str) -> float:
        expression = self.get_expression(num1, num2, operation)

        try:
            result: float = eval(expression)
            return float(result)
        except Exception as e:
            raise MathematicalException(f'The mathematical operation is not correct: {e}')
