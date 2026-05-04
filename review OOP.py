print("exercise: robot chữa cháy")
class Sensor:
    def __init__(self, smoke_level):
        self.smoke_level = smoke_level
    def get_smoke_level(self):
        return self.smoke_level
class Processor:
    def __init__(self):
        self.fire_detected = False
    def process_data(self, smoke_level):
        if smoke_level > 50:
            self.fire_detected = True
        elif smoke_level < 20:
            self.fire_detected = False
        return self.fire_detected
class Controller:
    def control_robot(self, fire_detected):
        if fire_detected:
            return "Shooting water."
        else:
            return "Stop shooting water."
# Example usage
smoke_sensor = Sensor(70)
smoke_level = smoke_sensor.get_smoke_level()
print(smoke_level)
data_processor = Processor()
fire_detected = data_processor.process_data(smoke_level)
print(fire_detected)
robot_controller = Controller()
print(robot_controller.control_robot(fire_detected))