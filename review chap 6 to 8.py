#exercise 1.1
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
#exercise 1.2
print("Exercise 1.2: Guard condition in FSM")
from enum import Enum
class MotorFSM:
    def __init__(self):
        self.state ="IDLE"
        self.motor_ok=True
    def handle_event(self, event):
        if self.state=="IDLE" and event=="START":
            if self.motor_ok:
                self.state="RUNNING"
                print("Motor started safely.")
            else:
                self.state="ERROR"
                print("Motor check failed - ERROR state.")
        elif self.state=="RUNNING" and event=="STOP":
            self.state="IDLE"
            print("Motor stopped.")
fsm = MotorFSM()
print(f"State: {fsm.state}")
fsm.handle_event("START")
print(f"State: {fsm.state}")
fsm.handle_event("STOP")
print(f"State: {fsm.state}")
fsm2=MotorFSM()
fsm2.motor_ok=False
fsm2.handle_event("START")
print(f"State: {fsm2.state}")
#exercise 1.3
print("Exercise 1.3: Door Lock FSM")
class DoorLock:
    def __init__(self):
        self.state = "LOCKED"
        self.attempts = 0
    def enter_code(self, code):
        if self.state == "LOCKED":
            if code == "1234":
                self.state = "UNLOCKED"
                self.attempts = 0
                print("Door unlocked.")
            else:
                self.attempts += 1
                print(f"Incorrect code. Attempt {self.attempts}.")
                if self.attempts >= 3:
                    self.state = "ALARM"
                    print("ALARM TRIGGERED !")
lock = DoorLock()
print(f"State: {lock.state}")
lock.enter_code("0000")
lock.enter_code("5678")
lock.enter_code("9999")
print(f"State: {lock.state}")
lock2= DoorLock()
lock2.enter_code("1234")
print(f"State: {lock2.state}")
