from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

redled = LED(17)
greenled = LED(27)
blueled = LED(22)

win = Tk()
win.title(“LED Toggler”)
myFont = tkinter.font.Font(family = ‘Helvetica’, size = 12, weight = “bold”)

def redledToggle():
       If redled.is_lit:
            redled.off()
            redledButton[“text”] = “Turn Red LED on”
      else:
            redled.on()
            redledButton[“text”] = “Turn Red LED off”

def greenledToggle():
       If greenled.is_lit:
            greenled.off()
            greenledButton[“text”] = “Turn Green LED on”
      else:
            greenled.on()
            greenledButton[“text”] = “Turn Green LED off”

def blueledToggle():
       If blueled.is_lit:
            blueled.off()
            blueledButton[“text”] = “Turn Blue LED on”
      else:
            blueled.on()
            blueledButton[“text”] = “Turn Blue LED off”


def close():
      RPi.GPIO.cleanup()
      win.destroy()


redledButton = Button(win, text = ‘Turn Red LED on’, font = myFont, command = redledToggle, bg = ‘red’, height = 1, width =24)
redledButton.grid(row=0,column=1)

greenledButton = Button(win, text = ‘Turn Green LED on’, font = myFont, command = greenledToggle, bg = ‘green’, height = 1, width =24)
greenledButton.grid(row=1,column=1)

blueledButton = Button(win, text = ‘Turn Blue LED on’, font = myFont, command = blueledToggle, bg = ‘blue’, height = 1, width =24)
blueledButton.grid(row=2,column=1)

exitButton = Button(win, text = ‘Exit, font = myFont, command = close, bg = ‘grey’, height = 1, width =24)
exitButton.grid(row=3,column=1)

win.protocol(“WM_DELETE_WINDOW”, close)

win.mainloop()
