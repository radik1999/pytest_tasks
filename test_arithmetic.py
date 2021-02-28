import pytest

from P7_T2 import arithmeti


class TestArithmetic:
    @pytest.mark.parametrize('a, b, result', [(6, 50, 56),
                                              (-10, 10, 0)])
    def test_plus_arithmetic(self, a, b, result):
        assert arithmeti(a, b, '+') == result

    @pytest.mark.parametrize('a, b, result', [(1, 2, -1),
                                              (100, 50, 50)])
    def test_minus_arithmetic(self, a, b, result):
        assert arithmeti(a, b, '-') == result

    @pytest.mark.parametrize('a, b, result', [(1, 2, 2),
                                              (-1, 0, 0)])
    def test_mult_arithmetic(self, a, b, result):
        assert arithmeti(a, b, '*') == result

    @pytest.mark.parametrize('a, b, result', [(4, 2, 2),
                                              (1, 0, None)])
    def test_div_arithmetic(self, a, b, result):
        assert arithmeti(a, b, '/') == result

    def test_unknown_operation(self):
        assert arithmeti(0, 0, 'plus') == 'Unknown operation'
