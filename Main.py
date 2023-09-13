# Import required libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set the mode for the GPIO pins
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
# Define LED pins
red = LED(14)
green = LED(15)
blue = LED(18)

### GUI DEFINITIONS ###
win = Tk()
win.title("LED Toggler")

# Define font for the GUI
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

### Event Functions ###
def toggle_red_led():
    """Toggle red LED and ensure other LEDs are off."""
    if red.is_lit:
        red.off()
    else:
        red.on()
        green.off()
        blue.off()

def toggle_green_led():
    """Toggle green LED and ensure other LEDs are off."""
    if green.is_lit:
        green.off()
    else:
        green.on()
        red.off()
        blue.off()

def toggle_blue_led():
    """Toggle blue LED and ensure other LEDs are off."""
    if blue.is_lit:
        blue.off()
    else:
        blue.on()
        red.off()
        green.off()

def close_program():
    """Cleanup GPIO pins and close the GUI."""
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###

# Red LED control button
redButton = Radiobutton(win, text='Toggle Red LED', font=myFont, command=toggle_red_led, bg='red', height=1, width=24)
redButton.grid(row=0, column=1)

# Green LED control button
greenButton = Radiobutton(win, text='Toggle Green LED', font=myFont, command=toggle_green_led, bg='green', height=1, width=24)
greenButton.grid(row=0, column=2)

# Blue LED control button
blueButton = Radiobutton(win, text='Toggle Blue LED', font=myFont, command=toggle_blue_led, bg='blue', height=1, width=24)
blueButton.grid(row=0, column=3)

# Exit button to close the GUI
exitButton = Button(win, text='Exit', font=myFont, command=close_program, bg='red', height=1, width=6)
exitButton.grid(row=2, column=2)

# Ensure that GPIO is cleaned up if the user closes the window using the 'X' button
win.protocol("WM_DELETE_WINDOW", close_program)

# Start the main GUI loop
win.mainloop()
