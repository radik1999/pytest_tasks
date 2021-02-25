import pytest

from P12_T1 import Model


@pytest.fixture
def model_object():
    return Model(0)


class TestModel:
    @pytest.mark.parametrize('year, result', [(1994, 2000), (2010, 2010), (2021, 2018)])
    def test_year_setter(self, model_object, year, result):
        model_object.year = year
        assert model_object.year == result

    @pytest.mark.parametrize('year, result', [(1999, "The car model is 2000"),
                                              (2005, "The car model is 2005"),
                                              (2022, "The car model is 2018")])
    def test_display(self, model_object, year, result):
        model_object.year = year
        assert model_object.display() == result
