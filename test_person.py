import pytest

from P11_HW1 import Person


class TestPerson:
    def test_compare_age_younger(self):
        person = Person('Viktor', 11)
        assert person.compare_age() == 'Viktor is younger than me.'

    def test_compare_age_older(self):
        person = Person('Viktor', 31)
        assert person.compare_age() == 'Viktor is older than me.'

    def test_compare_age_equal(self):
        person = Person('Viktor', 22)
        assert person.compare_age() == 'Viktor is the same age as me.'

    def test_negative_compare_age(self):
        person = Person('I', -1)
        assert person.compare_age() == "Person's age can't be a negative number"
