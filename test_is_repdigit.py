from pytest import mark


from tasks import is_repdigit


class TestIsRepdigit:
    @mark.parametrize('digit, result', [(66, True), (0, True), (-11, False)])
    def test_is_repdigit(self, digit, result):
        assert is_repdigit(digit) == result
