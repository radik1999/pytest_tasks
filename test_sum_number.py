import pytest

from P7_T1 import sum_numbers


class TestSumNumber:
    @pytest.mark.parametrize('str_number, result', [('123', 6),
                                                    ('567', 18),
                                                    ('1010', 2)])
    def test_sum_numbers(self, str_number, result):
        assert sum_numbers(str_number) == result

    def test_sum_none_numbers(self):
        assert sum_numbers('') == 0
