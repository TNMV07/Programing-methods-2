class Controller:
    """
    Functional Block: Controller
    Responsibility: Compute a motor command given the current sensor reading.
    This implementation uses a fixed step target (open-loop position command).
    """

    def __init__(self, target: float) -> None:
        self._target = target

    def set_target(self, target: float) -> None:
        self._target = target

    def compute(self, position: float) -> float:
        """Return the command to drive the joint toward the target position."""
        return self._target
