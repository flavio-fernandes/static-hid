# static-hid
Circuit Python based capacitive touch trigger for static keyboard strings

This is an easy project for using the
[Adafruit Neo Trinkey](https://www.adafruit.com/product/4870) as
a keyboard to type in static strings based on capacitive touch.

![Neo Trinkey](https://live.staticflickr.com/65535/51215237540_7a21314ab1_b.jpg)
    
In order to get going, do the following:

1) [Install Circuit Python](https://learn.adafruit.com/adafruit-neo-trinkey/circuitpython#circuitpython-quickstart-3087052-2)
on the device.
2) Create a file called secrets.py that contains the strings you want to be typed when you touch one of the 2 sensors.
Use [secrets.py.sample](https://github.com/flavio-fernandes/static-hid/blob/main/secrets.py.sample) as a reference.
3) Copy **code.py**, **secrets.py** and the **lib** directory to the mounted */Volumes/CIRCUITPY*
folder.
    
Check out [this page](https://learn.adafruit.com/neo-trinkey-case) for 3d printing a case for the Neo Trinkey.
    
Lastly, use [this guide](https://learn.adafruit.com/adafruit-neo-trinkey/capacitive-touch-hid) to learn all you need to know about this little gizmo.
