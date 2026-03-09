from pysimverse import Drone
import time
import keyboard

drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
rc_speed = 250

while True:
    #Get all values to 0
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if keyboard.is_pressed("w"):
        forward_backward = rc_speed
    elif keyboard.is_pressed("s"):
        forward_backward = -rc_speed
    elif keyboard.is_pressed("a"):
        left_right = -rc_speed
    elif keyboard.is_pressed("d"):
        left_right = rc_speed
    elif keyboard.is_pressed("f"):
        up_down = rc_speed
    elif keyboard.is_pressed("c"):
         up_down = -rc_speed
    elif keyboard.is_pressed("q"):
        yaw = -1
    elif keyboard.is_pressed("e"):
        yaw = 1 
    elif keyboard == ord("1") or keyboard == 27:
        drone.land()
        time.sleep(2)
        break

    drone.send_rc_control(left_right, forward_backward, up_down, yaw)
    time.sleep(0.05)

