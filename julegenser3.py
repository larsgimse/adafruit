from digitalio import DigitalInOut, Direction, Pull
import board
import neopixel
import time
from random import randint
try:
	import urandom as random  # for v1.0 API support
except ImportError:
	import random

pixpin = board.D1
numpix = 30
hue = 0



led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

button2 = DigitalInOut(board.D0)
button2.direction = Direction.INPUT
button2.pull = Pull.UP

strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.05, auto_write=True)

def colorWipe(color, wait):
    for j in range(len(strip)):
	strip[j] = (color)
	time.sleep(wait)

def color4Random(color, wait):
#    for step in range(3):

    strip[randint(0, numpix-1)] = (color)
#    strip[randint(0, 3)] = (color)
#    strip[randint(0, 3)] = (color)
#    strip[randint(0, 3)] = (color)
    time.sleep(wait)
#    strip[randint(0,29)] = (color)
#    strip[randint(0,29)] = (color)
#    strip[randint(0,29)] = (color)



def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(len(strip)):
            idx = int ((i * 256 / len(strip)) + j)
            strip[i] = wheel(idx & 255)
        time.sleep(wait)

def rainbow(wait):
    for j in range(255):
        for i in range(len(strip)):
            idx = int (i+j)
            strip[i] = wheel(idx & 255)

def rainbowOne():
    for i in range(len(strip)):
        idx = int ((i * 256 / len(strip)))
        strip[i] = wheel(idx & 255)
    strip.show()

def allStrip(color):
    for a in range(len(strip)):
        strip[a] = (color)

#led = -3
#ledCount = -3
red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)
off = (0,0,0)

color = wheel(hue & 255)

while True:
    # we could also just do "led.value = not button.value" !
    if button.value:
#        led.value = True
#           colorWipe( red, 0 )
#           strip.fill(blue)
#        strip.fill(off)
		i = random.randint(0, numpix - 1)  # Choose random pixel
		strip[i] = color   # Set it to current color
		strip.write()      # Refresh LED states
		# Set same pixel to "off" color now but DON'T refresh...
		# it stays on for now...bot this and the next random
		# pixel will be refreshed on the next pass.
		strip[i] = [0,0,0]
		time.sleep(0.008)  # 8 millisecond delay
           #rainbow(0.001)
#           colorRandom( (0, 255, 0) )
    elif button2.value:
        color4Random(white,.01)
        color4Random(off,.01)

    else:
#	       led.value = False
#           rainbow(0.05)
#        colorWipe( (0, 255, 0), 0 )
#        strip.fill( (255, 255, 255) )
#        strip.write()
#        allStrip ( (255,255,255) )
#        strip.fill(off)
#        color4Random(white,.1)
#        color4Random(off,.1)
        rainbowOne()

#        rainbow_cycle(0)



#    time.sleep(0.01) # debounce delay



#    clear()
#    if led < 33:
#        strip[led] = (255, 0, 0)
#        strip[led + 1] = (255, 0, 0)
#        strip[led + 3] = (255, 0, 0)
#        strip[led - 1] = (0, 0, 0)
#        strip[led + 4] = (255, 0, 0)
#        strip[led + 5] = (255, 0, 0)
#    strip.show()
#    time.sleep(0.1)
#        stripe.clear()
#        led = led + 1


#    strip[led - 1] = (0, 0, 0)
#    strip[led - 2] = (0, 0, 0)
#    strip[led - 1] = (0, 0, 0)

#    if led == 30:
#        for i in range(30):
#        strip[i] = (0, 0, 0)
#        led = 0

#    colorWipe( (255, 0, 0), .1 ) # red and delay
#    strip[randint(0,30)] = (0,0,0)
##    colorWipe( (0, 0, 255), .1)  # blue and delay

#    rainbow(0.05)
#    rainbow_cycle(0.05)
