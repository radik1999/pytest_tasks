from pytest import mark


from tasks import square_area


class TestSquareArea:
    @mark.parametrize('radius, result', [(5, 50), (6, 72), (7, 98)])
    def test_square_area(self, radius, result):
        assert square_area(radius) == result

