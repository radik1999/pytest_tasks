import pytest

from P7_HW6 import is_prime


class TestIsPrime:
    @pytest.mark.parametrize('number', [2, 3, 5])
    def test_is_prime(self, number):
        assert is_prime(number) is True

    @pytest.mark.parametrize('number', [4, 6, 8])
    def test_is_not_prime(self, number):
        assert is_prime(number) is False