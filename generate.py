import pyrosim.pyrosim as pyrosim


x = 0
y = 0
z = 0.5


pyrosim.Start_SDF("boxes.sdf")
for n in range(5):
    z = 0
    x = n
    length = 1
    width = 1
    height = 1
    for m in range(5):
        y = m
        z = 0
        length = 1
        width = 1
        height = 1
        for i in range(10):
            # kreiranje kutije
            name = f"box_{i}.sdf"
            pyrosim.Send_Cube(name, [x, y, z], [length, width, height])
            z = z+height
            length = length * 0.9
            height = height * 0.9
            width = width * 0.9

pyrosim.End()
