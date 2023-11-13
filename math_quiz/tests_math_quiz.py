import unittest
from math_quiz import number_choice, operation_choice, selecting_operation


class TestMathGame(unittest.TestCase):

    def test_number_choice(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = number_choice(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation_choice(self):
        total_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = operation_choice()
            self.assertIn(operator, total_operators)

    def test_selecting_operation(self):
        test_cases = [
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '*', '5 * 2', 10),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = selecting_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
