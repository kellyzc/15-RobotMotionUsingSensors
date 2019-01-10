"""
This module demonstrates lets you practice implementing classes and the
wait-until-event pattern, in the context of robot motion that uses sensors.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Zach Kelly.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import ev3dev.ev3 as ev3
import time
import math


def main():
    """ Calls the other functions to test/demo them. """
    run_test_wait_for_seconds()
    run_test_init()
    run_test_go_and_stop()
    run_test_go_straight_for_seconds()
    run_test_go_straight_for_inches()
    run_test_go_straight_until_black()


def run_test_wait_for_seconds():
    """ Tests the   wait_for_seconds   function by calling it. """
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_seconds   function:')
    print('--------------------------------------------------')

    wait_for_seconds()

    print('Here is a second test:')
    wait_for_seconds()


def wait_for_seconds():
    """ Prints Hello, waits for 3 seconds, then prints Goodbye. """
    # -------------------------------------------------------------------------
    # Done: 2. With your instructor, implement and test this function.
    #   IMPORTANT:  Do NOT use the    time.sleep   function
    #               anywhere in this project.
    #               (Exception: Use it in test-functions to separate tests.)
    #
    #               Instead, use the   time.time   function
    #               that returns the number of seconds since "the Epoch"
    #               (January 1, 1970, 00:00:00 (UTC) on some platforms).
    #
    #   The testing code is already written for you (above, in main).
    #   NOTE: this function has nothing to do with robots,
    #   but its concepts will be useful in the forthcoming robot exercises.
    # -------------------------------------------------------------------------
    print('Hello')
    start = time.time()
    while time.time() - start < 3:
        pass
    print('Goodbye')


def run_test_init():
    """ Tests the   __init__   method of the SimpleRoseBot class. """
    print()
    print('--------------------------------------------------')
    print('Testing the   __init__   method of the SimpleRoseBot class:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, then implement the   __init__   method
    #   of the SimpleRoseBot class, then use this function to test __init__.
    # -------------------------------------------------------------------------
    robot = SimpleRoseBot()
    robot.go(70, 70)
    start = time.time()
    while time.time() - start < 3:
        pass
    robot.stop()


def run_test_go_and_stop():
    """ Tests the   go   and   stop   methods of the SimpleRoseBot class. """
    print()
    print('--------------------------------------------------')
    print('Testing the  go  and  stop  methods of the SimpleRoseBot class:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Done: 4. Implement this function, then implement the   go  and   stop
    #   methods of the SimpleRoseBot class, then use this function
    #   to test both   go   and   stop   at the same time.
    # -------------------------------------------------------------------------
    robot = SimpleRoseBot()
    robot.go(40, 70)
    start = time.time()
    while time.time() - start < 3:
        pass
    robot.go(100, 0)
    start = time.time()
    while time.time() - start < 5:
        pass
    robot.stop()



def run_test_go_straight_for_seconds():
    """ Tests the   go_straight_for_seconds   method of SimpleRoseBot. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight_for_seconds   method of SimpleRoseBot:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Done: 5. Implement this function, then implement the
    #   go_straight_for_seconds   method of the SimpleRoseBot class,
    #   then use this function to test that method.
    # -------------------------------------------------------------------------
    robot = SimpleRoseBot()
    robot.go_straight_for_seconds(5, 50)
    robot.go_straight_for_seconds(10, 100)
    robot.stop()


def run_test_go_straight_for_inches():
    """ Tests the   go_straight_for_inches   method of SimpleRoseBot. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight_for_inches   method of SimpleRoseBot:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Done: 6. Implement this function, then implement the
    #   go_straight_for_inches   method of the SimpleRoseBot class,
    #   then use this function to test that method.
    # -------------------------------------------------------------------------
    robot = SimpleRoseBot()
    robot.go_straight_for_inches(5)
    robot.go_straight_for_inches(10)
    robot.stop()


def run_test_go_straight_until_black():
    """ Tests the   go_straight_until_black   method of SimpleRoseBot. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight_until_black   method of SimpleRoseBot:')
    print('--------------------------------------------------')
    # -------------------------------------------------------------------------
    # Done: 7. Implement this function, then implement the
    #   go_straight_until_black   method of the SimpleRoseBot class,
    #   then use this function to test that method.
    # -------------------------------------------------------------------------
    robot = SimpleRoseBot()
    robot.go_straight_until_black()
    robot.go_straight_until_black()
    robot.stop()


###############################################################################
# Put your   SimpleRoseBot    class here (below this comment).
# Your instructor may help you get started.
###############################################################################

class SimpleRoseBot(object):
    def __init__(self):
        self.left_wheel_motor = Motor('B')
        self.right_wheel_motor = Motor('C')
        self.color_sensor = ColorSensor(3)

    def go(self, left_speed, right_speed):
        self.left_wheel_motor.turn_on(left_speed)
        self.right_wheel_motor.turn_on(right_speed)

    def stop(self):
        self.left_wheel_motor.turn_off()
        self.right_wheel_motor.turn_off()

    def go_straight_for_seconds(self, seconds, speed):
        robot = SimpleRoseBot()
        robot.go(speed, speed)
        start = time.time()
        while time.time() - start < seconds:
            pass
        robot.stop()

    def go_straight_for_inches(self, inches):
        robot = SimpleRoseBot()
        robot.left_wheel_motor.reset_position()
        robot.go(25, 25)
        while robot.left_wheel_motor.get_position() / 360 * 1.3 * math.pi < inches:
            pass
        robot.stop()

    def go_straight_until_black(self):
        robot = SimpleRoseBot()
        robot.go(100, 100)
        while robot.color_sensor.get_reflected_light_intensity() > 20:
            pass
        robot.stop()


###############################################################################
# The  Motor   and   ColorSensor classes.  USE them, but do NOT modify them.
###############################################################################
class Motor(object):
    WheelCircumference = 1.3 * math.pi

    def __init__(self, port):  # port must be 'B' or 'C' for left/right wheels
        self._motor = ev3.LargeMotor('out' + port)

    def turn_on(self, speed):  # speed must be -100 to 100
        self._motor.run_direct(duty_cycle_sp=speed)

    def turn_off(self):
        self._motor.stop(stop_action="brake")

    def get_position(self):  # Units are degrees (that the motor has rotated).
        return self._motor.position

    def reset_position(self):
        self._motor.position = 0


class ColorSensor(object):
    def __init__(self, port):  # port must be 3
        self._color_sensor = ev3.ColorSensor('in' + str(port))

    def get_reflected_light_intensity(self):
        # Returned value is from 0 to 100,
        # but in practice more like 3 to 90+ in our classroom lighting.
        return self._color_sensor.reflected_light_intensity


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
