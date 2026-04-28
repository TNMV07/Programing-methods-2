# Exercise 1: Functional Decomposition of a Robotic Arm
## Functional Block Diagram
[User Task] --> [Task Planner] --> [Inverse Kinematics] --> [Motion Controller] --> [Actuators / Joints] --> [Robot Arm] -->[End Effector + Gripper] <-- [Sensors & Force Feedback]
## Candidate Classes
1. RobotArm
2. Joint
3. Gripper
4. ForwardKinematics
5. InverseKinematics
6. MotionController
7. Sensor
8. CollisionDetector
9. TaskPlanner
## Component Interaction
- TaskPlanner sends target position to InverseKinematics
- InverseKinematics computes joint angles
- MotionController sends commands to Joint
- Sensors provide feedback to Controller
- CollisionDetector checks workspace limits
## Justification
The system is decomposed into kinematics, control, sensing, and execution layers
to separate concerns. This improves modularity, maintainability, and scalability.
Each component handles a single responsibility.
# Exercise 2: Master-Slave Hierarchical Control Design
## 1. Device Level
Role: Hardware execution
### Slaves:
- Motor drivers
- LIDAR
- Camera
- IMU
- Battery sensors
### Commands received:
- PWM / velocity commands
- Start / stop sensing
### State reported:
- Motor speed feedback
- Raw sensor data
- Battery voltage
## 2. Master–Slave Definition per Level
### Level 3:
- Master: MissionController
- Slaves: Subsystems
- Commands down: mission goals, stop commands
- State up: system health, task completion
### Level 2:
- Master: Subsystem controllers
- Slaves: Device controllers
- Commands down: control parameters
- State up: processed sensor/state data
### Level 1:
- Master: Subsystem controller
- Slaves: Hardware devices
- Commands down: low-level signals
- State up: raw feedback
## 3. Architecture Diagram
## 1. 3-Level Master–Slave Hierarchy
### Level 3 – Mission Level
Role: High-level decision making
#### Master:
- MissionController
#### Slaves:
- Motion Subsystem
- Perception Subsystem
- Power Management Subsystem
#### Commands flow down:
- Set mission (patrol, follow wall, return to base)
- Enable / disable subsystems
- Emergency stop
#### State flows up:
- Mission status (RUNNING / DONE / ERROR)
- Obstacle detected
- Battery level status
### Level 2 – Subsystem Level
Role: Coordination inside each subsystem
#### Motion Control Subsystem:
- Master: MotionController
- Slaves: Motor controllers
- Commands down: linear velocity, angular velocity
- State up: speed, position estimate
#### Perception Subsystem:
- Master: PerceptionManager
- Slaves: LIDAR, Camera, IMU
- Commands down: sensor mode, sampling rate
- State up: obstacle map, orientation, vision result
#### Power Management Subsystem:
- Master: PowerManager
- Slave: Battery Management System
- Commands down: power limit, shutdown
## 4. Explanation
### Why this follows the Master–Slave pattern:
- Higher levels issue commands only
- Lower levels execute commands and report states
- Clear separation of decision making and execution
### What happens when a Slave reports ERROR:
- Error is sent to its Master
- Master escalates error upward
- MissionController triggers Emergency Stop if critical
### Adding a new sensor without changing Mission Level:
- Add sensor to the Perception Subsystem
- Mission Level remains unchanged
- Ensures modular and scalable design