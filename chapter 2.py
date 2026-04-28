#excercise 1
print("Exercise 1: Simple Euler Integration")
v,dt,g=0.0,0.1,-9.81
velocity=v-g*dt
print(f"Velocity after 0.1 seconds is {velocity:.2f} m/s")
#excercise 2
import matplotlib.pyplot as plt
print("Exercise 2: Free Oscillation of Mass–SpringDamper")
m=0.5
k=20.0
d=0.5
dt=0.01
t_end=5.0
position=0.1
velocity=0.0
time=[]
positions=[]
t=0.0
while t<t_end:
    acceleration=(-d*velocity-k*position)/m
    velocity=velocity+acceleration*dt
    position=position+velocity*dt
    time.append(t)
    positions.append(position)
    t+=dt
plt.plot(time,positions)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Free Oscillation of Mass–SpringDamper')
plt.grid()
plt.show()
