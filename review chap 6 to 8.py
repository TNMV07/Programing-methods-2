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
#exercise 2.1
print("Exercise 2.1: Find Maximum Sensor Value")
def find_max(readings):
    if not readings:
        raise ValueError("Cannot find max of empty list.")
    max_val=readings[0]
    for val in readings[1:]:
        if val>max_val:
            max_val=val
    return max_val
# Test 1: Normal case 
result = find_max([23.1, 26.4, 21.8, 29.3, 25.0]) 
print(result)                 # Should print: 29.3 
# Test 2: Negative values 
result = find_max([-5, -2, -10, -1]) 
print(result)                          # Should print: -1 
# Test 3: Single element 
result = find_max([42.5]) 
print(result)
#exercise 2.2
print("Exercise 2.2: Linear search")
def linear_search(robot_ids, target):
    for i in range(len(robot_ids)):
        if robot_ids[i] == target:
            return i
    return -1
#Test 1: Target found at index 2
result = linear_search([42, 17, 83, 5, 61], 83)
print(result)  # Should print: 2
#Test 2: Target at beginning
result = linear_search([10, 20, 30, 40], 10)
print(result)  # Should print: 0
# Test 3: Target not found
result = linear_search([1, 2, 3, 4, 5], 99)
print(result)  # Should print: -1
#exercise 2.3
print("Exercise 2.3: Selection sort")
def selection_sort(data):
    result = data.copy()
    n=len(result)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if result[j]<result[min_idx]:
                min_idx=j
        result[i],result[min_idx]=result[min_idx],result[i]
    return result
# Test 1: Unsorted floats
result = selection_sort([3.5, 1.2, 4.8, 0.9])
print(result)  # Should print: [0.9, 1.2, 3.5, 4.8]
# Test 2: Already sorted
result = selection_sort([1, 2, 3, 4])
print(result)  # Should print: [1, 2, 3, 4]
# Test 3: Reverse sorted
result = selection_sort([5, 4, 3, 2, 1])
print(result)  # Should print: [1, 2, 3, 4, 5]
#exercise 2.4
print("Exercise 2.4: Binary search")
def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#Test 1: Target found at index 3
result = binary_search([1, 3, 5, 7, 9, 11], 7)
print(result)  # Should print: 3
#Test 2: Target at beginning
result = binary_search([10, 20, 30, 40, 50], 10)
print(result)  # Should print: 0
# Test 3: Target at end
result = binary_search([10, 20, 30, 40, 50], 50)
print(result)  # Should print: 4
# Test 4: Target not found
result = binary_search([1, 3, 5, 7, 9], 4)
print(result)  # Should print: -1