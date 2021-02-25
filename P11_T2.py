# Create a coloredDoor class that has the 'color' attribute.
#
# Create a ClosedDoor class that has a default status of 'closed'.
#
# Create a ToggleDoor class that has a method toggle() that  toggles
# the status of the door.


class ColoredDoor:
    def __init__(self, color):
        self.color = color


class ClosedDoor(ColoredDoor):
    def __init__(self, color, status="closed"):
        super().__init__(color)
        self.status = status


class ToggleDoor(ClosedDoor):
    def __init__(self, color, status='closed'):
        super().__init__(color, status)

    def toggle(self):
        toggle_dict = {"opened": "closed", "closed": "opened"}
        self.status = toggle_dict[self.status]

