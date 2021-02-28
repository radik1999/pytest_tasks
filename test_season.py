import pytest

from P7_HW4 import season


class TestSeason:
    @pytest.mark.parametrize('number_of_month, seas', [(1, 'Winter'),
                                                       (5, 'Spring'),
                                                       (7, 'Summer'),
                                                       (10, 'Autumn')])
    def test_positive_season(self, number_of_month, seas):
        assert season(number_of_month) == seas

    def test_negative_season(self):
        assert season(21) is "There isn't such month"
