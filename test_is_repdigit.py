from pytest import mark

from tasks import is_repdigit


class TestIsRepdigit:
    @mark.parametrize('digit', [66, 0])
    def test_is_repdigit(self, digit):
        assert is_repdigit(digit)

    @mark.parametrize('digit', [32, -11])
    def test_is_not_repdigit(self, digit):
        assert is_repdigit(digit) is False
