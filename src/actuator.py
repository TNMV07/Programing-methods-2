class Actuator:
    """
    Functional Block: Actuator
    Responsibility: Accept a validated motor command and expose it to the simulation.
    Command range: [0.0, 6.29] rad (approx. 0 to 2π)
    """

    COMMAND_MIN = 0.0
    COMMAND_MAX = 6.29

    def __init__(self) -> None:
        self._command = 0.0

    def set_command(self, value: float) -> None:
        if not self.COMMAND_MIN <= value <= self.COMMAND_MAX:
            raise ValueError(
                f"Actuator command out of range: {value} "
                f"(valid: [{self.COMMAND_MIN}, {self.COMMAND_MAX}])"
            )
        self._command = value

    def command(self) -> float:
        return self._command
