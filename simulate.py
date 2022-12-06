import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import matplotlib.pyplot as plt
import random

pi = numpy.pi

amplitude_fl = pi/4
frequency_fl = 5
phaseOffset_fl = 1
amplitude_bl = pi/4
frequency_bl = 5
phaseOffset_bl = 0


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
print(robotId)
p.setGravity(0, 0, -9.81)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
back_leg_sensor_values = numpy.zeros(1000)
front_leg_sensor_values = numpy.zeros(1000)

angles = numpy.linspace(0, 2*pi, 1000)

back_leg_angles = amplitude_bl * numpy.sin(frequency_bl*angles + phaseOffset_bl)
front_leg_angles = amplitude_fl * numpy.sin(frequency_fl*angles + phaseOffset_fl)

numpy.save(file="data/frontLeg.npy", arr=front_leg_angles)
numpy.save(file="data/backLeg.npy", arr=back_leg_angles)

# exit()

for sec in range(1000):
    time.sleep(1/240)
    p.stepSimulation()

    back_leg_sensor_values[sec] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    front_leg_sensor_values[sec] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b"Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=front_leg_angles[sec], maxForce=100)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b"Torso_BackLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=back_leg_angles[sec], maxForce=100)


numpy.save(file="data/backLegSensorValues.npy", arr=back_leg_sensor_values)
numpy.save(file="data/frontLegSensorValues.npy", arr=front_leg_sensor_values)

p.disconnect()

