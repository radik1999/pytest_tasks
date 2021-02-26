import pytest


from P7_T2 import arithmeti


class TestArithmetic:
    def test_plus_arithmetic(self):
        assert arithmeti(1, 2, '+') == 3

    def test_minus_arithmetic(self):
        assert arithmeti(1, 2, '-') == -1

    def test_mult_arithmetic(self):
        assert arithmeti(1, 2, '*') == 2

    def test_div_arithmetic(self):
        assert arithmeti(4, 2, '/') == 2
