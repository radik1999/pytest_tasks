import pytest

from P11_T2 import ToggleDoor


class TestDoor:
    def test_positive_toggle_door_closed(self):
        door = ToggleDoor('red', status='closed')
        door.toggle()
        assert door.status == 'opened'

    def test_positive_toggle_door_opened(self):
        door = ToggleDoor('red', status='opened')
        door.toggle()
        assert door.status == 'closed'

    def test_negative_toggle_door(self):
        door = ToggleDoor('red', status='close')
        door.toggle()
        assert door.status == 'Status in the instant creation isn\'t correct'
