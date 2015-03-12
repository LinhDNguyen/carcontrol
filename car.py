#/usr/bin/env python2.7

import RPi.GPIO as GPIO
from time import sleep
import curses

motorLeft = None
motorRight = None

def config_gpio():
    global motorLeft
    global motorRight
    # Numbering by GPIO number, not header pin numberring
    GPIO.setmode(GPIO.BCM)

    # Use GPIO12 (PWM0) J8-32 to control speed of motor A
    #     GPIO13 (PWM1) J8-33 to control speed of motor B
    # Use GPIO07 J8-26   |
    #     GPIO08 J8-24  | to control direction of motor A
    # Use GPIO25 J8-22  |
    #     GPIO24 J8-18  | to control direction of motor B

    # Config pins
    # Motor A
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT, initial=0)
    GPIO.setup(8, GPIO.OUT, initial=0)
    motorLeft = GPIO.PWM(12, 1000)
    # Motor B
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT, initial=0)
    GPIO.setup(24, GPIO.OUT, initial=0)
    motorRight = GPIO.PWM(13, 1000)

    motorLeft.start(0)
    motorRight.start(0)

def left_dir(direction):
    if direction > 0:
        GPIO.output(7, 1)
        GPIO.output(8, 0)
    elif direction == 0:
        GPIO.output(7, 0)
        GPIO.output(8, 0)
    else:
        GPIO.output(7, 0)
        GPIO.output(8, 1)
def right_dir(direction):
    if direction > 0:
        GPIO.output(25, 1)
        GPIO.output(24, 0)
    elif direction == 0:
        GPIO.output(25, 0)
        GPIO.output(24, 0)
    else:
        GPIO.output(25, 0)
        GPIO.output(24, 1)
def stop():
    global motorLeft
    global motorRight
    left_dir(0)
    right_dir(0)
    motorLeft.ChangeDutyCycle(0)
    motorRight.ChangeDutyCycle(0)
def go(left, right):
    global motorLeft
    global motorRight
    ld = 1
    rd = 1
    if left < 0:
        ld = -1
    if right < 0:
        rd = -1
    left_dir(ld)
    right_dir(rd)
    motorLeft.ChangeDutyCycle(abs(left))
    motorRight.ChangeDutyCycle(abs(right))

def terminate():
    global motorLeft
    global motorRight
    # Stop and clean
    motorLeft.stop()
    motorRight.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    # Config screen
    # get the curses screen window
    screen = curses.initscr()

    # turn off input echoing
    curses.noecho()

    # respond to keys immediately (don't wait for enter)
    curses.cbreak()

    # map arrow keys to special values
    screen.keypad(True)

    try:
        config_gpio()
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_RIGHT:
                stop()
                sleep(0.2)
                screen.addstr(0, 0, 'right')
                go(100, -100)
            elif char == curses.KEY_LEFT:
                stop()
                sleep(0.2)
                screen.addstr(0, 0, 'left ')
                go(-100, 100)
            elif char == curses.KEY_UP:
                stop()
                sleep(0.2)
                screen.addstr(0, 0, 'up   ')
                go(100, 100)
            elif char == curses.KEY_DOWN:
                stop()
                sleep(0.2)
                screen.addstr(0, 0, 'down ')
                go(-100, -100)
            else:
                stop()
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        terminate()