import time
import board
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from secrets import TOUCH1_STR, TOUCH2_STR
import neopixel

# ref: https://learn.adafruit.com/adafruit-neo-trinkey/capacitive-touch-neopixel-brightness

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "purple": (255, 0, 255),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


def touched(touch, color, touch_str):
    if not touch.value:
        return
    start_touch = time.monotonic()
    pixels.fill(color)
    while touch.value:  # Wait for release...
        time.sleep(0.1)
        if time.monotonic() - start_touch > 3:
            pixels.fill(colors["red"])
            time.sleep(2)
            pixels.fill(colors["black"])
            return
    keyboard_layout.write(touch_str)
    pixels.fill(colors["black"])


for c in "purple", "cyan", "black":
    pixels.fill(colors[c])
    time.sleep(0.5)

while True:
    touched(touch1, colors["blue"], TOUCH1_STR)
    touched(touch2, colors["green"], TOUCH2_STR)
