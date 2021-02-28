from tasks import fizz_buzz


class TestFizzBuzz:
    def test_fizz(self):
        assert fizz_buzz(3) == 'Fizz'

    def test_buzz(self):
        assert fizz_buzz(5) == 'Buzz'

    def test_fizz_buzz(self):
        assert fizz_buzz(15) == 'FizzBuzz'

    def test_number(self):
        assert fizz_buzz(1) == '1'

    def test_negative_str(self):
        assert fizz_buzz('number') == 'int required'

