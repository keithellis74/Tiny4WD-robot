#!/usr/bin/python3

import piconzero
from approxeng.input.selectbinder import ControllerResource

robot = piconzero.Robot()

with ControllerResource() as joystick:
	while True:
		ly = joystick.axes.get_value('ly')
		ry = joystick.axes.get_value('ry')
		robot.set_motors(ly, ry)
