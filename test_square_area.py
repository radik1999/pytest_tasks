from pytest import mark

from tasks import square_area


class TestSquareArea:
    @mark.parametrize('radius, result', [(5, 50), (6, 72), (7, 98)])
    def test_square_area(self, radius, result):
        assert square_area(radius) == result

    def test_negative_square_area(self):
        assert square_area(-4) == 'A radius has to be a positive number'
