import time
import sys
import keyboard
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit


kit = MotorKit()
kit2 = MotorKit(address=0x61)

position_stack = []
a_axis_counter = 0
b_axis_counter = 0
c_axis_counter = 0
d_axis_counter = 0

def get_kit1():
	return kit
	
def get_kit2():
	return kit2

def shutdown():
    kit.stepper2.release()
    kit.stepper1.release()
    kit2.stepper1.release()
    kit2.stepper2.release()
    print("motor released from cancelation prompt")
    time.sleep(1)
    sys.exit()

# AXIS JOG CONFIG
def b_lower_arm():
    kit.stepper2.onestep(style=stepper.INTERLEAVE)
    #kit.stepper2.onestep(style=stepper.MICROSTEP)
    #kit.stepper2.onestep(style=stepper.DOUBLE)
    #kit.stepper2.onestep()
    global b_axis_counter
    b_axis_counter -= 1
    
def b_raise_arm():
    global b_axis_counter
    b_axis_counter += 1
    #kit.stepper2.onestep(direction=stepper.BACKWARD)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    
def a_axis_left():
    kit.stepper1.onestep()
    global a_axis_counter
    a_axis_counter -= 1
    
def a_axis_right():
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    global a_axis_counter
    a_axis_counter += 1
    
# kit no 2
def c_lower_swivel():
    kit2.stepper1.onestep(style=stepper.DOUBLE)
    global c_axis_counter
    c_axis_counter -= 1
    
def c_raise_swivel():
    kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    global c_axis_counter
    c_axis_counter += 1
    
# kit no 2
def d_rotate_left():
    kit2.stepper2.onestep(style=stepper.DOUBLE)
    global d_axis_counter
    d_axis_counter -= 1
    
def d_rotate_right():
    kit2.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    global d_axis_counter
    d_axis_counter += 1
