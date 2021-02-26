import pytest

from P7_HW5 import bank


class TestBank:
    @pytest.mark.parametrize('money, number_of_years, result', [(1000, 3, 1331),
                                                                (200, 2, 242),
                                                                (50000, 1, 55000)])
    def test_bank(self, money, number_of_years, result):
        assert bank(money, number_of_years) == result

