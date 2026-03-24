from robodk.robolink import *

# Connect to RoboDK
RDK = Robolink()

# Get robot
robot = RDK.Item('RDK-COBOT-1200', ITEM_TYPE_ROBOT)

# Get objects
bottle = RDK.Item('Bottle')   # make sure name matches RoboDK
box = RDK.Item('Box')
tool = robot.Tool()

if not robot.Valid():
    raise Exception("Robot not found")

if not bottle.Valid():
    raise Exception("Bottle not found")

if not box.Valid():
    raise Exception("Box not found")

# Get targets
home = RDK.Item('T1')
T1   = RDK.Item('T2')
T4   = RDK.Item('T3')

# Move to pick position
robot.MoveJ(pick)

# Close gripper (attach object)
RDK.AttachClosest()   # attaches bottle to tool

print("Picked bottle")

# Move up slightly (optional)
robot.MoveL(robot.Pose())

# Move to place position
robot.MoveJ(place)

# Open gripper (detach object)
RDK.DetachAll(tool)

print("Placed bottle")

# Return home
robot.MoveJ(home)

print("Done!")


while True:
    print("Moving to Home")
    robot.MoveJ(home)

    print("Moving to T1")
    robot.MoveJ(T1)

    print("Moving to T4")
    robot.MoveJ(T4)

    print("Returning to Home")
    robot.MoveJ(home)

    print("Movement completed")