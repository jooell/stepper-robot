import time
import sys
import keyboard
import board
import concurrent.futures
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import stepper_runners





def position_move(steps):				
	for coordinates in steps:
		print("recieved", coordinates)


		with concurrent.futures.ThreadPoolExecutor() as executor:
			futures = []
			
			changeA = (coordinates[0] - stepper_runners.a_axis_counter)	
			changeB = (coordinates[1] - stepper_runners.b_axis_counter)	

			for _ in range(abs(changeA)):
				if changeA > 0:
					futures.append(executor.submit(stepper_runners.a_axis_right))
				if changeA < 0:	
					futures.append(executor.submit(stepper_runners.a_axis_left))
					
			for _ in range(abs(changeB)):
				if (changeB) > 0:
					futures.append(executor.submit(stepper_runners.b_raise_arm))
				if (changeB) < 0:	
					futures.append(executor.submit(stepper_runners.b_lower_arm))
					
			concurrent.futures.wait(futures)
					


	
			"""
				# A axis rotation
				print(type(coordinates))
				changeA = (coordinates[0] - stepper_runners.a_axis_counter)	
				if (changeA) > 0:					
					print(f'going up {changeA} steps')
					for i in range(changeA):			
						stepper_runners.a_axis_right()
						time.sleep(0.01)
						
				if (changeA) < 0:					
					changeA = (changeA * -1)	
					print(f'going down {changeA} steps')
					for i in range(changeA):			
						stepper_runners.a_axis_left()
						time.sleep(0.01)
						
				# B axis rotation		
				changeB = (coordinates[1] - stepper_runners.b_axis_counter)	
				if (changeB) > 0:					
					print(f'going up {changeB} steps')
					for i in range(changeB):			
						stepper_runners.b_raise_arm()
						time.sleep(0.01)
						
				if (changeB) < 0:					
					changeB = (changeB * -1)	
					print(f'going down {changeB} steps')
					for i in range(changeB):			
						stepper_runners.b_lower_arm()
						time.sleep(0.01)
			"""
