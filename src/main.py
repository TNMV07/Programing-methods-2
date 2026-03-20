from system_info import SystemInfo
from sensor import Sensor
from controller import Controller
from actuator import Actuator
from simulation import Simulation
from logger import Logger

MODEL_PATH = "/home/openmind/VGU/Programming_Method_2/PM2/example/chapter2/assets/motor_1dof.xml"


def main() -> None:
    system = SystemInfo("1-DOF Motor System", "2.0")
    print(system.describe())

    # --- Instantiate the 5 functional blocks ---
    sim        = Simulation(model_path=MODEL_PATH)
    sensor     = Sensor(sim.data)
    controller = Controller(target=3.0)
    actuator   = Actuator()
    log        = Logger()

    # --- Step loop: Sensor → Controller → Actuator → Simulation → Logger ---
    def step() -> None:
        position = sensor.joint_position()
        command  = controller.compute(position)
        actuator.set_command(command)
        log.record(sim.time, command, position)
        sim.step(actuator.command())

    sim.run(duration=5.0, step_callback=step, viewer=True)

    print("Final joint position:", sensor.joint_position())
    log.plot("position_control_plot.png")


if __name__ == "__main__":
    main()
