import pytest


from P7_HW2 import is_year_leap


class TestIsYearLeap:
    @pytest.mark.parametrize('year', [2016, 2020, 2000])
    def test_is_year_leap(self, year):
        assert is_year_leap(year) is True

    @pytest.mark.parametrize('year', [1999, 2001, 2022])
    def test_is_not_leap(self, year):
        assert is_year_leap(year) is False

    def test_negative_is_leap(self):
        assert is_year_leap(-4) is None
