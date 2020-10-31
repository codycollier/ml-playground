

## Adafruit & Arduino IDE - Setup


#### References: 
* download: https://www.arduino.cc/en/software
* https://learn.adafruit.com/adafruit-pybadge/setup
* https://learn.adafruit.com/adafruit-pybadge/using-with-arduino-ide
* https://learn.adafruit.com/adafruit-pybadge/arcada-libraries
* https://learn.adafruit.com/tensorflow-lite-for-edgebadge-kit-quickstart/setup-for-compiling-examples


#### Steps:
```
Download and install arduino ide
. All notes here use 1.9.0-beta for Mac OS X


ide: arduino ide -> preferences -> board manager urls
. add adafruit url: https://adafruit.github.io/arduino-board-index/package_adafruit_index.json


ide: arduino ide -> Tools -> Board -> Board Managers
. install Arduino SAMD
. install Adafruit SAMD
. restart, updates, etc


ide: arduino ide -> Tools -> Manage Libraries
. install Adafruit Arcada Libraries (includes a lot of deps)
. install Arduino_TensorFlowLite (1.15.0-Alpha, not precompiled)
    . note: 2.1.0-alpha is available (presumably matching tf2)
. install Adafruit TensorFlow Lite
. install Zero PDM (1.2.0)


ide: arduino ide -> Tools -> Board
. board: select `Adafruit pyBadge M4 express (SAMD51)` from tree
. cpu: overclock to 180
. usb stack: tiny usb
. port: serial (usb) /dev/cu.usbmodem14401
    . note: watch out for bad / charge only cables


```





