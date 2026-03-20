from typing import List

import matplotlib.pyplot as plt


class Logger:
    """
    Functional Block: Logger / Visualization
    Responsibility: Record simulation data each timestep and plot results.
    """

    def __init__(self) -> None:
        self.times: List[float] = []
        self.commands: List[float] = []
        self.positions: List[float] = []

    def record(self, time: float, command: float, position: float) -> None:
        self.times.append(time)
        self.commands.append(command)
        self.positions.append(position)

    def plot(self, save_path: str = "simulation_plot.png") -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(self.times, self.commands, label="Command (Position)", linestyle="--")
        plt.plot(self.times, self.positions, label="Output (Joint Position)")
        plt.xlabel("Time (s)")
        plt.ylabel("Joint position (rad)")
        plt.title("Motor Simulation (Position Control): Command vs Output")
        plt.legend()
        plt.grid(True)
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
        plt.close()
