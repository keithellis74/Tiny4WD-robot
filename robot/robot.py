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
debug = False
running = True
detect_joystick = True
run_motors = True
tank_mode = False

#functions
def _print(item):
	if debug == True:
		print(item)

def robot_cleanup():
	robot.stop()

def mixer(yaw, throttle, max_power=1):
    """
    Mix a pair of joystick axes, returning a pair of wheel speeds. This is where the mapping from
    joystick positions to wheel powers is defined, so any changes to how the robot drives should
    be made here, everything else is really just plumbing.

    :param yaw:
        Yaw axis value, ranges from -1.0 to 1.0
    :param throttle:
        Throttle axis value, ranges from -1.0 to 1.0
    :param max_power:
        Maximum speed that should be returned from the mixer, defaults to 100
    :return:
        A pair of power_left, power_right integer values to send to the motor driver
    """
    left = throttle + yaw
    right = throttle - yaw
    scale = float(max_power) / max(1, abs(left), abs(right))
    return float(left * scale), float(right * scale)

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
				if tank_mode:
					# Check and react to joystick input
					ly = joystick['ly']
					ry = joystick['ry']
					_print("Left y = {0}".format(ly))
					_print("Right y = {0}".format(ry))
					sleep(0.1)
					if run_motors:
						robot.set_motors(ly, ry)
					else:
						_print("Motors not enabled")
						_print ("left = {}, right = {}".format(l, r))

				#Running with left stick only
				else:
					yaw = joystick['lx']
					throttle = joystick['ly']
					_print("Yaw = {0}".format(yaw))
					_print("Thottle = {0}".format(throttle))
					sleep(0.1)
					l, r = mixer(yaw, throttle)
					if run_motors:
						_print ("left = {}, right = {}".format(l, r))
						robot.set_motors(l, r)
					else:
						_print ("left = {}, right = {}".format(l, r))

				# Check and react to button presses
				presses = joystick.check_presses()
				held = joystick['select']
				if held is not None and held > 5:
					_print("Start held for more than 5 seconds")
					running = False
					robot_cleanup()
					os.system("/sbin/halt")
				if presses['r1']:
					tank_mode = not tank_mode
					print("Tankmode = {}".format(tank_mode))

	except IOError:
		_print("No joystick found")
		sleep(0.3)

