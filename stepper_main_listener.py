import time
import sys
import keyboard
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import stepper_runners
#from stepper_main_listener import keyboard_listener
import stepper_advanced_movements
import stepper_main_listener



def keyboard_listener():
	while True:
		# disable
		if keyboard.is_pressed('space'):
			stepper_runners.shutdown()
			break
			
		# safety
		if keyboard.is_pressed('a') and keyboard.is_pressed('d'):
			continue
		if keyboard.is_pressed('q') and keyboard.is_pressed('e'):
			continue
		
		# B lower axis
		if keyboard.is_pressed('s') and not keyboard.is_pressed('w'):
			stepper_runners.b_lower_arm()
			while keyboard.is_pressed('s') and not keyboard.is_pressed('w'):
				time.sleep(0.01)
				stepper_runners.b_lower_arm()
				
		# B raise axis
		if keyboard.is_pressed('w') and not keyboard.is_pressed('s'):
			stepper_runners.b_raise_arm()
			while keyboard.is_pressed('w') and not keyboard.is_pressed('s'):
				time.sleep(0.01)
				stepper_runners.b_raise_arm()
					  
		# A AXIS LEFT Q
		if keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
			stepper_runners.a_axis_left()
			while keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
				time.sleep(0.01)
				stepper_runners.a_axis_left()
		
		# A AXIS RIGHT E
		if keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
			stepper_runners.a_axis_right()
			while keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
				time.sleep(0.01)
				stepper_runners.a_axis_right()
		
		# C lower swivel
		if keyboard.is_pressed('q') and not keyboard.is_pressed('e'):
			stepper_runners.c_lower_swivel()
			while keyboard.is_pressed('q') and not keyboard.is_pressed('e'):
				time.sleep(0.01)
				stepper_runners.c_lower_swivel()
				
		# C raise swivel        
		if keyboard.is_pressed('e') and not keyboard.is_pressed('q'):
			stepper_runners.c_raise_swivel()
			while keyboard.is_pressed('e') and not keyboard.is_pressed('q'):
				time.sleep(0.01)
				stepper_runners.c_raise_swivel()
				
		# D rotate left
		if keyboard.is_pressed('j') and not keyboard.is_pressed('l'):
			stepper_runners.d_rotate_left()
			while keyboard.is_pressed('j') and not keyboard.is_pressed('l'):
				time.sleep(0.01)
				stepper_runners.d_rotate_left()
				
		# D rotate right
		if keyboard.is_pressed('l') and not keyboard.is_pressed('j'):
			stepper_runners.d_rotate_right()
			while keyboard.is_pressed('l') and not keyboard.is_pressed('j'):
				time.sleep(0.01)
				stepper_runners.d_rotate_right()
				
				
				
				
					
		# test simulativ
		if keyboard.is_pressed('x'):
			print('A = {0} B = {1} C = {2} D = {3}'.format(stepper_runners.a_axis_counter, stepper_runners.b_axis_counter, stepper_runners.c_axis_counter, stepper_runners.d_axis_counter))
			stepper_runners.position_stack.append([stepper_runners.a_axis_counter, stepper_runners.b_axis_counter, stepper_runners.c_axis_counter, stepper_runners.d_axis_counter])
			time.sleep(0.2)

		# test simulativ
		if keyboard.is_pressed('b'):
			stepper_advanced_movements.position_move(stepper_runners.position_stack) # target B position
			time.sleep(0.2)
			
		if keyboard.is_pressed('h'):
			print('Homing home')
			stepper_advanced_movements.position_move([[0, 0, 0, 0]])
			time.sleep(0.2)
