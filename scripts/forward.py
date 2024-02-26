#!/usr/bin/env python3
from adafruit_crickit import crickit
import time
import os
from enum import Enum

DC_ADJUST_R = float(os.environ.get("ROBO_DC_ADJUST_R", "1.0"))
DC_ADJUST_L = float(os.environ.get("ROBO_DC_ADJUST_L", "1.0"))
ADJUST = dict(R=DC_ADJUST_R, L=DC_ADJUST_L)
MOTOR = dict(R=crickit.dc_motor_1, L=crickit.dc_motor_2)
THROTTLE_SPEED = {0: 0, 1: 0.5, 2: 0.7, 3: 0.9} # 0.3 minimum speed but unreliable

class Direction(Enum):
    FWD = 1
    STOP = 0
    REV = -1

def set_throttle(name: str, newSpeed=0, direction=Direction.STOP):
    
    print("START: ")
    print(direction)
    
    if direction.name not in Direction._member_names_:
        print("ENTERED: ")
        print(direction)
        direction = Direction.STOP

    MOTOR[name].throttle = THROTTLE_SPEED[newSpeed] * ADJUST[name] * direction.value


def forward(duration=0.2, speed=3):
    set_throttle("R", speed, Direction.FWD)
    set_throttle("L", speed, Direction.REV)
    time.sleep(duration)
    set_throttle("R", 0)
    set_throttle("L", 0)


for speed in [1, 2]:
    print("move forward at speed:", speed)
    forward(duration=1, speed=speed)
