from pytest import mark


from tasks import check_lines


class TestCheckLines:
    @mark.parametrize('a, b, c,')
    def test_check_lines_parallel(self):
        assert False

    def test_check_lines_not_parallel(self):
        assert False

