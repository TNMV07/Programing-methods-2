print("Exercise 1: Encapsulation (The Safe Gipper)")
class Gripper:
    def __init__(self):
        self._pressure = 0

    def get_status(self):
        return self._pressure

    def apply_pressure(self, pressure):
        if 0 <= pressure <= 100:
            self._pressure = pressure
        else:
            raise ValueError("Safety Limit Exceeded !")
safe_gripper = Gripper()
safe_gripper.apply_pressure(50)
print(f"Safe Gripper Status: {safe_gripper.get_status()}")
try:
    safe_gripper.apply_pressure(120)
except ValueError as e:
    print(e)
print("Exercise 2: Inheritance (Actuator Types)")
class Actuator:
    def __init__(self, pin_number):
        self.pin_number = pin_number
class Led(Actuator):
    def turn_on(self):
        print(f"LED on pin {self.pin_number} is glowing.")
class Buzzer(Actuator):
    def beep(self):
        print(f"Buzzer on pin {self.pin_number} is making sound.")
led = Led(5)
buzzer = Buzzer(7)
led.turn_on()
buzzer.beep()
print("Exercise 4: The Smart Cooling Fan")
class Fan:
    def __init__(self, temperature):
        self.temperature = temperature
    def system(self):
        if self.temperature > 40:
            print(f"Temperature: {self.temperature} Fan is ON")
        else:
            print(f"Temperature: {self.temperature} Fan is OFF")
Fan(45).system()
Fan(30).system()
print("Exercise 5: Automated Drill Cycle")
class Drill:
    def __init__(self, spin, pattern):
        self.spin = spin
        self.pattern = pattern
    def drill_cycle(self):
        print(f"Drill is spinning for {self.spin} seconds and retracting. This happens {self.pattern} times for a {self.pattern}-hole pattern.")
drill = Drill(3, 5)
drill.drill_cycle()