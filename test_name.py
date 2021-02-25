import pytest

from P11_HW3 import Name


class TestName:
    @pytest.mark.parametrize('firstname, lastname, fullname, initials', [
        ('Rodion', 'Tulub', 'Rodion Tulub', 'R.T.'),
        ('Vasia', 'Bubkin', 'Vasia Bubkin', 'V.B.'),
        ('Ivan', 'Ivanov', 'Ivan Ivanov', 'I.I.')
    ])
    def test_name(self, firstname, lastname, fullname, initials):
        name = Name(firstname, lastname)
        assert name.fullname == fullname and name.initials == initials
