import board
import neopixel
import time
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from secrets import TOUCH1_STR, TOUCH2_STR, TOUCH3_STR

# ref: https://learn.adafruit.com/adafruit-neo-trinkey/capacitive-touch-neopixel-brightness

COLORS = {
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


def _clear_pixels():
    pixels.fill(COLORS["black"])


def _touched_1():
    return touch1.value, COLORS["blue"], TOUCH1_STR


def _touched_2():
    return touch2.value, COLORS["green"], TOUCH2_STR


def _check_touched_both(touch_str):
    if _touched_1()[0] and _touched_2()[0]:
        pixels.fill(COLORS["cyan"])
        return True, TOUCH3_STR
    return False, touch_str


def _touched():
    return _touched_1()[0] or _touched_2()[0]


def check_touch():
    touched, color, touch_str = _touched_1()
    if not touched:
        touched, color, touch_str = _touched_2()
    if not touched:
        return
    start_touch = time.monotonic()
    pixels.fill(color)
    touched_both = False
    while _touched():
        time.sleep(0.1)
        # check if both were touched
        if not touched_both:
            touched_both, touch_str = _check_touched_both(touch_str)
        # if touch went for too long, forgetaboutit
        if time.monotonic() - start_touch > 3:
            pixels.fill(COLORS["red"])
            time.sleep(2)
            touch_str = None
            break
    if touch_str:
        keyboard_layout.write(touch_str)
    _clear_pixels()


for c in COLORS.values():
    pixels.fill(c)
    time.sleep(0.15)

_clear_pixels()
while True:
    check_touch()
