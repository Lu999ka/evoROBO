import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
p.setGravity(0, 0, -9.81)
p.loadSDF("box.sdf")

for sec in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
p.disconnect()

