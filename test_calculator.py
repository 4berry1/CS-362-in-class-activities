
import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.sub(4, 2)

    def test_mult(self):
        assert 8 == calculator.mult(4, 2)

    def test_devide(self):
        assert 2 == calculator.devide(4, 2)
