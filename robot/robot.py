#!/usr/bin/python3

#    robot.py - Program to control a Tiny4WD robot using the approxeng.input
#    joypad library by Tom Oinn and the 4Tronix motor controller board
#    Copyright (C) 2017  Keith Ellis

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.


# Code to drive 4 wheeled robot with piconzero motor driver
# both left wheels are driven by a single channel (1st) and right 
# wheels are driven by the 2nd channel.

# Using piconzero library written by Keith Ellis, based on sample code
# provided by 4Tronix
# Using joystick controller by Tom Oinn - approxeng.input
# https://github.com/ApproxEng

# imports
import piconzero
from approxeng.input.selectbinder import ControllerResource
from time import sleep
import os

# Set debug to true if you want extra debug info
debug = True
running = True
detect_joystick = True
run_motors = True

#functions
def _print(item):
	if debug == True:
		print(item)

def robot_cleanup():
	robot.stop()

# Main code
# Create robot object
try:
	robot = piconzero.Robot(debug = True)
except:
	_print("unable to create robot obejct, is piconzero board connected?")
	if debug == True:
		raise


# detect joystick inputs
while detect_joystick:
	try:
		with ControllerResource() as joystick:
			detect_joystick = False
			_print("Found joystick{}".format(joystick))
			while running:
				# Check and react to joystick input
				ly = joystick.axes.get_value('ly')
				ry = joystick.axes.get_value('ry')
				_print("Left y = {0}".format(ly))
				_print("Right y = {0}".format(ry))		
				sleep(0.1)
				if run_motors:
					robot.set_motors(ly, ry)
				else:
					print("Motors not enabled")

				# Check and react to button presses
				presses = joystick.buttons.get_and_clear_button_press_history()
				held = joystick.buttons.is_held_name('select')
				if held is not None and held > 5:
					_print("Start held for more than 5 seconds")
					running = False
					robot_cleanup()
					os.system("/sbin/halt")

	except IOError:
		_print("No joystick found")
		sleep(0.3)

