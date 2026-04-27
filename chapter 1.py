#exercise 2
print("Exercise 2: Sensor Data Cleaning")
text=" TEMP_DATA:25.678 "
cleaned = text.strip()
print(f"Cleaned string: '{cleaned}'")
value_str = cleaned.replace("TEMP_DATA:", "")
print(f"Extracted value string: '{value_str}'")
temperature = float(value_str)
print(f"Temperature: {temperature:.2f} °C")
#exercise 3
print("Exercise 3: Actuator Command Filtering")
torques=[1.2,5.5,0.8,10.2,4.9,-2.1,7.0]
safe_torques = [t for t in torques if abs(t)<=5.0]
safe_torques.append(0.0)
print("Safe torques:", safe_torques)
#exercise 4
print("Exercise 4:  Robot State Handling")
raw_gps=(10.823,106.629,5.0)
lat,lon,_=raw_gps
print(f"Latitude: {lat}, Longitude: {lon}")
def get_velocity():
    vx, vy = 0.5, 0.3
    return vx, vy
vel_x, vel_y = get_velocity()
print(f"Velocity X: {vel_x}, Velocity Y: {vel_y}")
#exercise 5
print("Exercise 5: Sensor Management")
sensor_cfg={"id":101,"type":"LIDAR","range":[0.1,30.0]}
sensor_cfg["range"]=[0.1,50.0]
sensor_cfg["status"]="active"
print("Updated sensor configuration:", sensor_cfg)
active_types=["Lidar","Camera","Lidar","IMU","Camera"]
unique_types=set(active_types)
print("Unique sensor types:", unique_types)
#exercise 6
print("Exercise 6: Safety Interlock System")
def safety_mode(dist,emergency_stop):
    if emergency_stop==True:
        return "ESTOP"
    elif dist<0.5:
        return "COLLISION"
    elif 0.5<=dist<1.0:
        return "WARNING"
    else:
        return "NORMAL"
mode=safety_mode(0.8,False)
print("Safety mode:", mode)
#exercise 7
print("Exercise 7: Battery Polling & Logging")
voltages=[12.6,12.5,12.2,11.8,11.5,10.8,10.2]
for Minutes,Voltage in enumerate(voltages):
    print(f"Minute {Minutes}: Voltage={Voltage:.2f}V")
v= 12.0
while v>10.5:
    v-=0.5
    if v<=10.5:
        print(f"Low Battery!: {v}V")
        break
for v in voltages:
    if v>12.0:
        continue
    elif v<11.0:
        print("Stop!")
        break
    else:
        print(f"Voltage: {v}V")
#exercise 8
print("Exercise 8: Motor Control Supervisor")
def set_motor_command(rpm: float, motor_id: int = 0):
    if rpm >1000:
        raise ValueError("Safety Limit Exceeded")
    return (motor_id, rpm)
try:
    cmd = set_motor_command(1200,1)
except ValueError as e:
    print("Error:", e)
cmd = set_motor_command(500,1)
print("Motor command:", cmd)
#exercise 9
print("Exercise 9: Simulated Sensor Data Logger")
class PressureSensor:
    def __init__(self, pressure):
        self._pressure = pressure
    def update_reading(self,value:float):
        if not (0.0 <= value <= 10.0):
            raise ValueError("ValueError")
        self._pressure = value
    @property
    def pressure(self):
        return self._pressure
sensor=PressureSensor(5.0)
sensor_log=[]
readings=[2.5,4.8,11.0]
for i, value in enumerate(readings):
    try:
        sensor.update_reading(value)
        sensor_log.append({
            "id": i,
            "val": sensor.pressure,
            "status": "OK"
        }) 
    except ValueError:
        sensor_log.append({
            "id": i,
            "val": value,
            "status": "ERROR"
        })
print(sensor_log)
#exercise 10
print("Exercise 10: Robotic Reachability & Profiling")
import math
import datetime
def arm_length():
    return 1.5
def target_angle_deg():
    return 30.0
starttime=datetime.datetime.now()
rad=target_angle_deg() * math.pi / 180
x=arm_length() * math.cos(rad)
y=arm_length() * math.sin(rad)
endtime=datetime.datetime.now()
duration=(endtime-starttime).microseconds
print(f"End-effector position: ({x:.3f}, {y:.3f})")
print(f"Duration: {duration} microseconds")
#excerise 11
print("Exercise 11: Multi-Axis IMU Data Processing")
import numpy as np
data = np.array([0.1, 0.2, 9.8, 0.15, 0.22, 9.78, 0.12, 0.21, 9.81, 0.11, 0.23, 9.79])
print("Shape:", data.shape)
print("Dtype:", data.dtype)
reshaped_data = data.reshape(4, 3)
print("IMU matrix:\n", reshaped_data)
print("Total elements:", reshaped_data.size)
#exercise 12
print("Exercise 12: Sensor Fusion & Sorting")
sensor_left = np.array([1.5,0.8,2.3])
sensor_right = np.array([2.1,0.5,1.9])
all_readings = np.concatenate((sensor_left, sensor_right))
print("All sensor readings:", all_readings)
sorted_readings = np.sort(all_readings)
print("Sorted sensor readings:", sorted_readings)
reshaped_data = all_readings.reshape(3, 2)
print("Reshaped sensor data:\n", reshaped_data)
#exercise 13
print("Exercise 13: Robot Sensor Data Extraction")
period_1 = np.array([[10,11,12],[20,21,22]])
period_2 = np.array([[30,31,32],[40,41,42]])
full_data= np.vstack((period_1, period_2))
print("Full sensor data:\n", full_data)
print("Slicing:")
print(full_data[:, 1])
print("Indexing:")
print(full_data[2:4, 1:3])
data_backup = full_data.copy()
print("Data backup:\n", data_backup)
#exercise 14
print("Exercise 14: Sensor Bias Correction")
raw_acel=np.array([[0.1, 0.1, 9.9], [0.1, 0.1, 9.9], [0.2, 0.0, 9.8], [0.1, 0.2, 9.9]])
bias=np.array([0.1, 0.1, 9.8])
cleaned_acel = raw_acel - bias
print("Cleaned accelerometer data:\n", cleaned_acel)
convert=cleaned_acel * 9.81
print("Converted g to m/s^2:\n", convert)
#exercise 15
print("Exercise 15: System Performance Analysis")
rng = np.random.default_rng()
power_consumption = rng.uniform(0.0, 10.0, size=(4,5))
print("Power consumption data:\n", power_consumption)
total_power = np.sum(power_consumption)
print(f"Total power consumption: {total_power:.2f}")
average_power = np.mean(power_consumption,axis=1)
print(f"Average power consumption: {average_power}")
peak_power = np.max(power_consumption,axis=0)
print(f"Peak power consumption: {peak_power}")
transposed_data = power_consumption.reshape(5,4)
print("Transposed data:\n", transposed_data)
#exercise 16
print("Exercise 16: Random Numbers and Statistics")
rng = np.random.default_rng()
matrix=rng.uniform(0.0, 1.0, size=(5,5))
print("Matrix:\n", matrix)
mean_value = np.mean(matrix)
std_value = np.std(matrix)
print(f"Mean value: {mean_value:.2f}, Std detection: {std_value:.2f}")
max_value = np.max(matrix)
print("Row maxs:", matrix.max(axis=1))
#exercise 17
print("Exercise 17: Filtering and Unique Counts")
data=rng.integers(1, 6, size=20)
print("Data:", data)
print("Filtered:",data[data > 3])
values, counts = np.unique(data, return_counts=True)
print("Unique values:", values)
print("Counts:", counts)
#exercise 18
print("Exercise 18: CSV Data Processing")
import pandas as pd
data=rng.random((10,3))
print("Sensor data:\n", data)
np.savetxt('sensor_data.csv', data, delimiter=',', header='Time,Temp,Volt', comments='')
df=pd.read_csv('sensor_data.csv')
print("First 5 rows:\n", df.head())
average_temp = round(df['Temp'].mean(),1)
print(f"Average temperature: {average_temp:.2f}")