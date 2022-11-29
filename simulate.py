import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import math

pi = math.pi

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

for sec in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    back_leg_sensor_values[sec] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    front_leg_sensor_values[sec] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b"Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=+pi/4, maxForce=500)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b"Torso_BackLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=-pi/4, maxForce=500)
    

numpy.save(file="data/backLegSensorValues.npy", arr=back_leg_sensor_values)
numpy.save(file="data/frontLegSensorValues.npy", arr=front_leg_sensor_values)
p.disconnect()

