import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0, 0, -9.81)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
back_leg_sensor_values = numpy.zeros(1000)
print(back_leg_sensor_values)

for sec in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    back_leg_sensor_values[sec] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
numpy.save(file="data/data.npy", arr=back_leg_sensor_values)
p.disconnect()

