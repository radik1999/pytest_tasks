from pytest import mark


from tasks import list_of_multiples


class TestListOfMultiples:
    @mark.parametrize('number, length, result', [(7, 5, [7, 14, 21, 28, 35]),
                                                 (12, 10, [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]),
                                                 (17, 6, [17, 34, 51, 68, 85, 102])])
    def test_list_of_multiples(self, number, length, result):
        assert list_of_multiples(number, length) == result
