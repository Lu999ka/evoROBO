import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for sec in range(1000):
    time.sleep(1/60)
p.disconnect()

