# Control an LED Matrix through Raspberry Pi & Tkinter

# Importing Libraries
from tkinter import *
from time import sleep
import RPi.GPIO as GPIO


BS1 = False


def led1(num):
    global BS1
    GPIO.setmode(GPIO.BOARD)
    red1 = 11
    GPIO.setup(red1, GPIO.OUT)
    GPIO.output(red1, True)
    if BS1 == False:
        GPIO.output(red1, 1)
        BS1 = True
        sleep(0.5)
    else:
        GPIO.output(red1, False)
        BS1 = False
        sleep(0.5)


BS2 = False


def led2(num):
    global BS2
    GPIO.setmode(GPIO.BOARD)
    yellow1 = 12
    GPIO.setup(yellow1, GPIO.OUT)
    GPIO.output(yellow1, True)

    if BS2 == False:
        GPIO.output(yellow1, 1)
        BS2 = True
        sleep(0.5)
    else:
        GPIO.output(yellow1, False)
        BS2 = False
        sleep(0.5)


BS3 = False  # trace LED status


def led3(num):
    global BS3
    GPIO.setmode(GPIO.BOARD)
    red2 = 13
    GPIO.setup(red2, GPIO.OUT)
    GPIO.output(red2, True)

    if BS3 == False:

        GPIO.output(red2, 1)
        BS3 = True
        sleep(0.5)
    else:
        GPIO.output(red2, False)
        BS3 = False
        sleep(0.5)


BS4 = False


def led4(num):
    global BS4
    GPIO.setmode(GPIO.BOARD)
    red3 = 15
    GPIO.setup(red3, GPIO.OUT)
    GPIO.output(red3, True)
    if BS4 == False:

        GPIO.output(red3, 1)
        BS4 = True
        sleep(0.5)
    else:
        GPIO.output(red3, False)
        BS4 = False
        sleep(0.5)


BS5 = False


def led5(num):
    global BS5
    GPIO.setmode(GPIO.BOARD)
    red4 = 16
    GPIO.setup(red4, GPIO.OUT)
    GPIO.output(red4, True)
    if BS5 == False:

        GPIO.output(red4, 1)
        BS5 = True
        sleep(0.5)
    else:
        GPIO.output(red4, False)
        BS5 = False
        sleep(0.5)


BS6 = False


def led6(num):
    global BS6
    GPIO.setmode(GPIO.BOARD)
    red5 = 18
    GPIO.setup(red5, GPIO.OUT)
    GPIO.output(red5, True)

    if BS6 == False:

        GPIO.output(red5, 1)
        BS6 = True
        sleep(0.5)
    else:
        GPIO.output(red5, False)
        BS6 = False
        sleep(0.5)


root = Tk()

# Buttons
button_1 = Button(root, text="1", height=2, width=3, command=lambda: led1(1))
button_1.grid(column=0, row=0)


button_2 = Button(root, text="2", height=2, width=3, command=lambda: led2(2))
button_2.grid(column=1, row=0)

button_3 = Button(root, text="3", height=2, width=3, command=lambda: led3(3))
button_3.grid(column=2, row=0)


button_4 = Button(root, text="4", height=2, width=3, command=lambda: led4(4))
button_4.grid(column=0, row=1)


button_5 = Button(root, text="5", height=2, width=3, command=lambda: led5(5))
button_5.grid(column=1, row=1)

button_6 = Button(root, text="6", height=2, width=3, command=lambda: led6(6))
button_6.grid(column=2, row=1)


root.mainloop()
