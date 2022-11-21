import pyrosim.pyrosim as pyrosim


x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube("Box", [x+3, y+3, z], [length, width, height])
    pyrosim.End()


# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     pyrosim.Send_Cube("Link0", [0, 0, 0.5], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])
#     pyrosim.Send_Cube("Link1", [0, 0, 0.5], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1])
#     pyrosim.Send_Cube("Link2", [0, 0, 0.5], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])
#     pyrosim.Send_Cube("Link3", [0, 0.5, 0], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 1, 0])
#     pyrosim.Send_Cube("Link4", [0, 0.5, 0], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 0.5, -0.5])
#     pyrosim.Send_Cube("Link5", [0, 0, -0.5], [1, 1, 1])
#     pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -1])
#     pyrosim.Send_Cube("Link6", [0, 0, -0.5], [1, 1, 1])
#     pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube("Torso", [1.5, 0, 1.5], [1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube("BackLeg", [-0.5, 0, -0.5], [1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube("FrontLeg", [0.5, 0, -0.5], [1, 1, 1])
    pyrosim.End()


Create_World()
Create_Robot()
