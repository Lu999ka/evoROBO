import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = 0


pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube("box_0.sdf", [x, y, z], [length, width, height])
pyrosim.Send_Cube("box_1.sdf", [x, y, z], [length, width, height])


pyrosim.End()
