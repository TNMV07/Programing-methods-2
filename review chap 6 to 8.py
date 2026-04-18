print("Exercise 1.1: Simple Traffic Light FSM")
from enum import Enum
class TrafficLightState(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
class Light:
    def __init__(self):
        self.state = TrafficLightState.RED

    def next_state(self):
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED
# Example usage
light = Light()
print(light.state)
light.next_state()
print(light.state)
light.next_state()
print(light.state)
light.next_state()
print(light.state)
