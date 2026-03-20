import mujoco
import mujoco.viewer
import numpy as np

model = mujoco.MjModel.from_xml_path("car.xml")
data = mujoco.MjData(model)
R = 5
L = -0.005

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():

        v = 10        # forward speed
        w = 2.0       # constant angular velocity

        v_left  = v - (L/2)*w
        v_right = v + (L/2)*w

        data.ctrl[0] =v_left  / 10*R
        data.ctrl[1] = v_right / R

        mujoco.mj_step(model, data)
        viewer.sync()