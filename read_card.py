import evdev
import RPi.GPIO as GPIO
import time
from evdev.ecodes import keys
from evdev.events import KeyEvent


def read_card():
 device = evdev.InputDevice('/dev/input/event0')
 device.grab()
 cardid  = ''
 for event in device.read_loop():

##Read only key pressed events i.e event type is key and is pressed down
  if event.type == evdev.ecodes.EV_KEY and event.value == KeyEvent.key_down:
    digit = str(keys[event.code])[4:] #Strip 'KEY_' characters from key_code 
    if digit == 'ENTER':
       device.ungrab()
       return cardid
    else:
       cardid += digit
 device.ungrab()

#Function is called if scanned card is authorised
def signal_auth():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(18,GPIO.OUT)
  GPIO.output(18,GPIO.HIGH)
  time.sleep(3)
  GPIO.output(18,GPIO.LOW)

#Function is called if scanned card is not authorised
def signal_notauth():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(23,GPIO.OUT)
  GPIO.output(23,GPIO.HIGH)
  time.sleep(3)
  GPIO.output(23,GPIO.LOW)

