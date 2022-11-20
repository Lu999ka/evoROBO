import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube("box.sdf", [0, 0, 0.5], [1, 1, 1])

pyrosim.End()
