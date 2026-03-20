import time
from typing import Callable

import mujoco
import mujoco.viewer


class Simulation:
    """
    Functional Block: Simulation
    Responsibility: Emulate physics using MuJoCo.
    Accepts a control command each step; owns no controller or sensor logic.
    """

    def __init__(self, model_path: str) -> None:
        self._model = mujoco.MjModel.from_xml_path(model_path)
        self._data = mujoco.MjData(self._model)
        self._time = 0.0

    @property
    def data(self) -> mujoco.MjData:
        return self._data

    @property
    def time(self) -> float:
        return self._time

    @property
    def timestep(self) -> float:
        return self._model.opt.timestep

    def step(self, command: float) -> None:
        """Apply command and advance physics by one timestep."""
        self._data.ctrl[0] = command
        mujoco.mj_step(self._model, self._data)
        self._time += self._model.opt.timestep

    def run(self, duration: float, step_callback: Callable[[], None], viewer: bool = True) -> None:
        """
        Run the simulation loop.

        :param duration:      Total simulation time in seconds.
        :param step_callback: Called once per timestep; responsible for reading
                              the sensor, computing the command, logging, and
                              calling self.step().
        :param viewer:        Launch the MuJoCo passive viewer if True.
        """
        steps = int(duration / self.timestep)

        if viewer:
            with mujoco.viewer.launch_passive(self._model, self._data) as v:
                for _ in range(steps):
                    if not v.is_running():
                        break
                    step_callback()
                    v.sync()
                    time.sleep(self.timestep)
        else:
            for _ in range(steps):
                step_callback()
