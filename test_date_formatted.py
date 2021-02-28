from pytest import mark


from tasks import date_formatted


class TestDateFormatted:
    @mark.parametrize('dat, result', [("11/12/2019", "20191211"), ("12/31/2019", "20193112"), ("01/15/2019", "20191501")])
    def test_date_formatted(self, dat, result):
        assert date_formatted(dat) == result

    @mark.parametrize('dat, result', [('1 January 1994', 'Wrong date format'),
                                      ('21/2/2022', 'Wrong date format')])
    def test_negative_date_formatted(self, dat, result):
        assert date_formatted(dat) == result