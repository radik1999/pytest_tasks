from pytest import mark


from tasks import check_lines


class TestCheckLines:
    @mark.parametrize('l1, l2', [([1, 2, 3], [1, 2, 4]),
                                 ([0, 1, 5], [0, 1, 5])])
    def test_check_lines_parallel(self, l1, l2):
        assert check_lines(l1, l2)

    @mark.parametrize('l1, l2', [([2, 4, 1], [4, 2, 1]),
                                 ([3, 2, 1], [1, 2, 3])])
    def test_check_lines_not_parallel(self, l1, l2):
        assert check_lines(l1, l2) is False

