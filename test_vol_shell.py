from pytest import mark


from tasks import vol_shell


class TestVolShell:
    @mark.parametrize('r1, r2, volume', [(3, 3, 0), (7, 2, 1403.245), (3, 800, 2144660471.753)])
    def test_vol_shell(self, r1, r2, volume):
        assert vol_shell(r1, r2) == volume

