<<<<<<< HEAD
import mujoco
import mujoco.viewer
import numpy as np

model = mujoco.MjModel.from_xml_path("turtlebot.xml")
data = mujoco.MjData(model)

R = 0.05
L = 0.32

obstacles = [
    np.array([1, 0]),
    np.array([2, 0.5]),
    np.array([2, -0.5])
]

def get_yaw(quat):
    w, x, y, z = quat
    return np.arctan2(
        2*(w*z + x*y),
        1 - 2*(y*y + z*z)
    )

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():

        x = data.qpos[0]
        y = data.qpos[1]

        theta = get_yaw(data.qpos[3:7])

        # ======================
        # 🎯 HƯỚNG THEO PATH (y=0)
        # ======================
        path_vec = np.array([1.0, -y])   # tiến theo x + kéo về y=0
        path_vec = path_vec / np.linalg.norm(path_vec)

        # ======================
        # 🚧 HƯỚNG TRÁNH VẬT CẢN
        # ======================
        avoid_vec = np.array([0.0, 0.0])

        for obs in obstacles:
            dx = x - obs[0]
            dy = y - obs[1]
            dist = np.sqrt(dx**2 + dy**2)

            if dist < 0.5:
                repulse = np.array([dx, dy]) / (dist + 1e-5)
                avoid_vec += repulse / dist   # càng gần càng mạnh

        # ======================
        # 🔥 COMBINE VECTOR
        # ======================
        total_vec = path_vec + 2.0 * avoid_vec

        # normalize
        if np.linalg.norm(total_vec) > 0:
            total_vec = total_vec / np.linalg.norm(total_vec)

        # ======================
        # 🎯 ĐỔI SANG GÓC
        # ======================
        target_angle = np.arctan2(total_vec[1], total_vec[0])

        angle_error = target_angle - theta
        angle_error = (angle_error + np.pi) % (2*np.pi) - np.pi

        # ======================
        # 🚗 CONTROL
        # ======================
        v = 0.5
        w = 2 * angle_error

        # giảm tốc khi gần obstacle
        if np.linalg.norm(avoid_vec) > 0:
            v = 0.3

        v_left  = v - (L/2)*w
        v_right = v + (L/2)*w

        data.ctrl[0] = v_left / R
        data.ctrl[1] = v_right / R

        mujoco.mj_step(model, data) 
=======
import mujoco
import mujoco.viewer

xml = """
<mujoco>
  <worldbody>
    <body pos="0 0 1">
      <geom type="sphere" size="0.1"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
>>>>>>> 670b68cf7db7f7afc642f5dc4cde45e142584976
        viewer.sync()