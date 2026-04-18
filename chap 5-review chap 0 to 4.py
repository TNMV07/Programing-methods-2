#chap 0 exercise 1
print("chapter 0 exercise 1")
from abc import ABC, abstractmethod
class Drone(ABC):
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
    def launch(self): None
class Fixedwing(Drone):
    def launch(self):
        print(f'Fixedwing {self.name} is taking off on a runway.')
class Quadcopter(Drone):
    def launch(self):
        print(f'Quadcopter {self.name} is spinning up 4 rotors.')
fleet = [Fixedwing("Eagle"), Quadcopter("Hawk")]
for drone in fleet:    
    drone.launch()
#chap 0 exercise 2
print("\nchapter 0 exercise 2")
class Fueltank:
    def __init__(self, capacity: float):
        self.__capacity = capacity
        self.__level = 0
    def fill(self, amount: float):
        if self.__level + amount > self.__capacity:
            print("Overflow prevented!")
        else:
            self.__level += amount
            print("OK, current level:", self.__level)
    def drain(self, amount: float)-> None:
        if self.__level - amount < 0:
            print("Cannot drain below 0!")
        else:            
            self.__level -= amount
            print("OK, current level:", self.__level)
    @property
    def level(self):
        return self.__level
tank = Fueltank(capacity=100)
tank.fill(60)
tank.fill(80)
tank.drain(20)
tank.drain(200)
print(tank.level)
#chap 0 exercise 3
print("\nchapter 0 exercise 3")
class ConveyorBelt:
    def __init__(self, speed_rpm: float):
        self.speed_rpm = speed_rpm
class LinearBelt(ConveyorBelt):
    def __init__(self, speed_rpm: float):
        super().__init__(speed_rpm)
    def run(self)-> None:
        print(f"Linear belt running at {self.speed_rpm} RPM.")
class SortingBelt(ConveyorBelt):
    def __init__(self, speed_rpm: float):
        super().__init__(speed_rpm)
    def run(self)-> None:
        print(f"Sorting belt running at {self.speed_rpm} RPM.")
    def sort_items(self, item: str)-> None:
        print(f"Sorting item by weight...")
belt = LinearBelt(speed_rpm=30)
sorter = SortingBelt(speed_rpm=20)
belt.run()
sorter.run()
sorter.sort_items(["Linear", "Sorting", "Belt"])
print(sorter.speed_rpm) 
#chap 0 exercise 4
print("\nchapter 0 exercise 4")
class PowerUnit:
    def diagnose(self)-> None:
        print("PowerUnit: Voltage 24.0V-OK")
class CoolingFan:
    def diagnose(self)-> None:
        print("CoolingFan: Temperature 45.0C-OK")
class NetworkCard:
    def diagnose(self)-> None:
        print("NetworkCard: Ping 12 ms-OK")
components = [PowerUnit(), CoolingFan(), NetworkCard()]
for c in components:
    c.diagnose()
#chap 1 exercise 1
print("\nchapter 1 exercise 1")
raw= "[Warn] MotorTemp:87.3"
test= raw.split()
print("print test:", test)
parts=raw.strip().split()
print("print parts[0]:", parts[0])
print("print parts[1]:", parts[1])
level=parts[0].replace("[","").replace("]","")
print("print level:", level)
value=parts[1].split(":")[1]
print("print value:", value)
print(f'Level: {level}, Value: {value}')
#chap 1 exercise 2
print("\nchapter 1 exercise 2")
readings=[0.1,0.3,15.7,0.2,0.4,18.2,0.3]
filtered_list = [a for a in readings if abs(a) <= 2.0]
print("Filtered list:", filtered_list)
compute_mean = sum(filtered_list) / len(filtered_list) if filtered_list else 0
print(f'Mean of filtered list: {compute_mean:.2f}')
#chap 1 exercise 3
print("\nchapter 1 exercise 3")
sequence=[10,9,8,7,6,5,"FAULT",3,2,1,"LAUNCH"]
for v in sequence:
    if isinstance(v, str) and v == "FAULT":
        print("Abort! Launch cancelled.")
        break
    elif isinstance(v, int) and v % 2 == 1:
        print(f"T-{v}:GO")
#chap 1 exercise 4
print("\nchapter 1 exercise 4")
joint_state=(1.57,0.25,3.2,72.0)
angle,velocity,torque,temperature_C = joint_state[:4]
_ = temperature_C
def get_offsets()->tuple:
    return(0.05,0.10)
angle_off, torque_off = get_offsets()
print(f"Angle: {angle} rad Velocity: {velocity} rad/s")
print(f"Offsets ->Angle: {angle_off:.2f} rad,torque: {torque_off:.2f} Nm")
#chap 1 exercise 5
print("\nchapter 1 exercise 5")
def classify_temp(t:float)-> str:
    if t<18.0:
        print(f"{t}: Cold")
    elif 18.0 <= t < 35.0:
        print(f"{t}: Normal")
    elif 35<= t < 70.0:
        print(f"{t}: Hot")
    else:
        print(f"{t}: Critical - shutdown!")
classify_temp(15.0)
classify_temp(25.0)
classify_temp(40.0)
classify_temp(85.0)
#chap 1 exercise 6
print("\nchapter 1 exercise 6")
readings=[10.1,9.3,12.4,11.8,11.6,11.7,11.65]
stable_count=0
for i,v in enumerate(readings):
    if i ==0:
        continue
    if abs(v-readings[i-1])<=0.5:
        stable_count +=1
    else:
        stable_count=0
    print(f"Reading {i}: {v}-unstable")
    if stable_count >=3:
        print(f"Stable at {v}")
        break
#chap 1 exercise 7
print("\nchapter 1 exercise 7")
def safe_average(values: list)->float|str:
    if len(values)==0:
        return "No data"
    sum = 0
    for v in values:
        sum +=v
    avg= sum/len(values)
    return avg
print(safe_average([3.0,5.0,4.0]))
print(safe_average([]))
print(safe_average([7.5]))
#chap 1 exercise 8
print("\nchapter 1 exercise 8")
def countdown(n:int)-> None:
    while n>0:
        if n%3==0:
            n-=1
            continue
        print(n)
        n-=1
    print("LIFTOFF")
countdown(10)
#chap 2 exercise 1
print("\nchapter 2 exercise 1")
import math
class JointAngle:
    def __init__(self): 
        self._degrees = 0.0
    def set_degrees(self, value: float):
        if not (-180 <= value <= 180):
            raise ValueError(f"Value Error: {value} is out of range [-180;180]!")
        self._degrees = value
    @property
    def degrees(self)-> float:
        return self._degrees
    @property
    def radians(self)-> float:
        return self._degrees * math.pi / 180
j=JointAngle()
j.set_degrees(90)
print(j.degrees)
print(f"{j.radians:.4f}")
try:
    j.set_degrees(200)
except ValueError as e:
    print(e)
#chap 2 exercise 2
print("\nchapter 2 exercise 2")
v,dt, g=1.0,0.1,-9.81
for i in range(10):
    t=i*dt
    print(f"t={t:.1f}s: v={v:.2f} m/s")
    v = v+g*dt
#chap 2 exercise 3
T,T_env,k,dt=80.0,20.0,0.1,1.0
while T>21.0:
    T = T - k*(T-T_env)*dt
    t+=dt
    print(f"t={t:.1f}s  T={T:.2f}C")
#chap 3 exercise 1
print("\nchapter 3 exercise 1")
class SpeedSensor:
    def __init__(self,rpm:float=0.0):
        self.rpm = rpm
    def measure(self)-> float:
        return self.rpm +0.5
class SpeedController:
    def __init__(self, kp: float=2.0):
        self.kp = kp
    def control(self, target: float, measured: float)-> float:
        return self.kp * (target - measured)
class EventLogger:
    def __init__(self):
        self.history = []
    def record(self,value:float)->None:
        self.history.append(round(value, 4))
    def report(self)-> None:
        print(f"History: {self.history}")
#chap 4 exercise 1
print("\nchapter 4 exercise 1")
from enum import Enum
class LightState(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
class TrafficLight:
    def __init__(self):
        self._state = LightState.RED
    @property
    def state(self):
        return self._state
    def transition(self, event: str):
        if event == "TICK":
            if self._state == LightState.RED: self._state = LightState.GREEN
            elif self._state == LightState.GREEN: self._state = LightState.YELLOW
            elif self._state == LightState.YELLOW: self._state = LightState.RED
light = TrafficLight()
for _ in range(6):
    print(light.state.name,end="  ")
    light.transition("TICK")
#chap 4 exercise 2
print("\nchapter 4 exercise 2")
from enum import Enum,auto
class state(Enum):
    IDLE = auto()
    COIN_IN = auto()
    DISPENSING = auto()
class VendingMachine:
    def __init__(self):
        self._state = state.IDLE
    @property
    def state(self):
        return self._state
    def transition(self, event: str) ->str|None:
        if self._state == state.IDLE and event == "INSERT_COIN":
            self._state = state.COIN_IN
        elif self._state == state.COIN_IN and event == "SELECT_ITEM":
            self._state = state.DISPENSING
        elif self._state == state.DISPENSING and event == "DONE":
            self._state = state.IDLE
        elif self._state == state.IDLE and event == "CANCEL":
            self._state = state.IDLE
        return None
machine = VendingMachine()
events = ["INSERT_COIN", "SELECT_ITEM", "DONE", "INSERT_COIN", "CANCEL"]
for e in events:
    print(f"Event: {e} -> State: {machine.state.name}")
    result = machine.transition(e)