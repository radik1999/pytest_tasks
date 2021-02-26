import pytest
import math

from P7_HW3 import square


class TestSquare:
    @pytest.mark.parametrize('side, result', [(2, (8, 4, math.sqrt(8))),
                                              (3, (12, 9, math.sqrt(18))),
                                              (4, (16, 16, math.sqrt(32)))])
    def test_square(self, side, result):
        assert square(side) == result

