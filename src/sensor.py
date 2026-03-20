import test_mujoco


class Sensor:
    """
    Functional Block: Sensor
    Responsibility: Provide joint position by reading from MuJoCo simulation data.
    """

    def __init__(self, data: test_mujoco.MjData) -> None:
        self._data = data

    def joint_position(self) -> float:
        return float(self._data.qpos[0])
