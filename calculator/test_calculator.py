# Unit tests for the Calculator library

import calculator


class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 4 == calculator.subtract(6, 2)
