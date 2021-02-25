from pytest import mark

from tasks import identify_student


class TestIdentifyStudent:
    @mark.parametrize('name, greeting', [
        ("Randy", "Hi! I'm Randy, and I'm from Germany."),
        ("Sam", "Hi! I'm Sam, and I'm from Argentina."),
        ("Monti", "Hi! I'm a guest.")
    ])
    def test_identify_student(self, name, greeting):
        assert identify_student(name) == greeting


