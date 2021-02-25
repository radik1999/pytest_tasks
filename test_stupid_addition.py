from pytest import mark


from tasks import stupid_addition


class TestStupidAddition:
    @mark.parametrize('par1, par2, result', [(1, 2, "12"), ("1", "2", 3)])
    def test_stupid_addition_same_type(self, par1, par2, result):
        assert stupid_addition(par1, par2) == result

    def test_stupid_addition_different_type(self):
        assert stupid_addition("1", 2) is None
