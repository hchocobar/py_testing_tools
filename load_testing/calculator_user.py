from locust import HttpUser, task, between


class CalculatorUser(HttpUser):
    wait_time = between(0, 1)

    @task(3)
    def calculate(self):
        self.client.post('/maths/calculate', json={'op1': 1, 'op2': 1, 'operation': 'multiplication'})

    @task
    def get_expression(self):
        self.client.post('/maths/expression', json={'op1': 1, 'op2': 1, 'operation': 'add'})
