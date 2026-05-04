import time
import random
class Sensor:
    def __init__(self):
        self.smoke_level = 0
    def read_data(self):
        self.smoke_level = random.randint(0, 100)
        return self.smoke_level
class Processor:
    def __init__(self):
        self.fire_detected = False
        self.fire_start_time = None
        self.no_fire_start_time = None
    def process_data(self, smoke_level):
        current_time = time.time()
        if smoke_level > 50:
            if self.fire_start_time is None:
                self.fire_start_time = current_time
            self.no_fire_start_time = None
            if current_time - self.fire_start_time >= 3:
                self.fire_detected = True
        elif smoke_level < 20:
            if self.no_fire_start_time is None:
                self.no_fire_start_time = current_time
            self.fire_start_time = None
            if current_time - self.no_fire_start_time >= 10:
                self.fire_detected = False
        return self.fire_detected
class Controller:
    def control_robot(self, fire_detected):
        if fire_detected:
            return "Shooting water"
        else:
            return "Stop shooting water"
sensor = Sensor()
processor = Processor()
controller = Controller()
print("Start system...\n")
for i in range(30):  # chạy 30 chu kỳ (~30 giây)
    smoke = sensor.read_data()
    fire = processor.process_data(smoke)
    action = controller.control_robot(fire)
    print(f"Smoke: {smoke:3} | Fire: {fire} | Action: {action}")
    time.sleep(1)  # mỗi vòng 1 giây