#!/bin/bash

#    start_robot,shy is a bash script to start the robot code, it is 
#    intended to be called from crontab or similar
#    Copyright (C) 2017  Keith Ellis

 #   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
 #   the Free Software Foundation, either version 3 of the License, or
 #   any later version.


 #   This program is distributed in the hope that it will be useful,
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.


/home/pi/repo/robot/robot.py 2>> /home/pi/log_robot_error.txt &
