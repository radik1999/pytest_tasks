from pytest import mark

from tasks import concat


class TestConcat:
    @mark.parametrize('lists, result', [
        ([[1, 2, 3], [4, 5], [6, 7]], [1, 2, 3, 4, 5, 6, 7]),
        ([[1], [2], [3], [4], [5], [6], [7]], [1, 2, 3, 4, 5, 6, 7]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[4, 4, 4, 4, 4]], [4, 4, 4, 4, 4])
    ])
    def test_concat(self, lists, result):
        assert concat(*lists) == result
