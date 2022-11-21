import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0, 0, -9.81)
p.loadSDF("world.sdf")

for sec in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
p.disconnect()

