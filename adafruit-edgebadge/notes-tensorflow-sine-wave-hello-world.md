

## Notes on running TensorFlow Sine Wave Demo on Adafruit EdgeBadge

#### References

* https://learn.adafruit.com/tensorflow-lite-for-edgebadge-kit-quickstart/sine-wave-demo


#### Prepare / Connect

```
device:
. plug in with usb cable
. turn on via on/off switch
. tap reset button twice to get into usb mode
. should show up as a usb device and screen should show PyBadge (v3.7.0)


ide: arduino ide -> Tools -> Board
. board: select `Adafruit pyBadge M4 express (SAMD51)` from tree
. cpu: overclock to 180
. usb stack: tiny usb
. port: serial (usb) /dev/cu.usbmodem14401
    . note: watch out for bad / charge only cables

```


#### Drag and drop a UF2 

There's a pre-compiled UF2. Download it, then drop it onto the device via mounted usb drive.

* https://cdn-learn.adafruit.com/assets/assets/000/083/188/original/pybadge_arcada_sinewave.UF2?1572324514

The UF2 is the version with arcada and on-screen output.


#### Hello_World: Select, compile, and upload the code 

Try out the non-screen version, which uses the serial plotter.

Note: The plain hello_world example at `Arduino_TensorFlowLite -> hello_world` is supposed to work according to the web page. It doesn't seem to work though, as the serial plotter never connects or shows output. It could be a mismatch with the arduino libs, arduino ide, etc. Instead of chasing that down I jumped to the adafruit `hellow_world_arcada` which has the screen output and works like the pre-compiled UF2 noted above.

```
# tried both hellow_world versions and the first has led output, 
# but neither works with serial plotter
ide: arduino ide -> File -> Examples -> Arduino_TensorFlowLite
ide: arduino ide -> File -> Examples -> Adafruit TensorFlow Lite
. select hello_world
. click the Upload button (arrow)
. observe
```

Arduino IDE output for writing to flash

```
Sketch uses 114560 bytes (22%) of program storage space. Maximum is 507904 bytes.
Device       : ATSAMD51x19
Version      : v1.1 [Arduino:XYZ] Jun 23 2019 17:44:35
Address      : 0x0
Pages        : 1024
Page Size    : 512 bytes
Total Size   : 512KB
Planes       : 1
Lock Regions : 32
Locked       : none
Security     : false
BOD          : false
BOR          : true
Write 116160 bytes to flash (227 pages)

[                              ] 0% (0/227 pages)
[=                             ] 3% (8/227 pages)
[==                            ] 7% (16/227 pages)
[===                           ] 10% (24/227 pages)
--snip--
[============================= ] 98% (224/227 pages)
[==============================] 100% (227/227 pages)
Done in 1.405 seconds
Verify 116160 bytes of flash

[=                             ] 3% (8/227 pages)
[=                             ] 3% (9/227 pages)
[=                             ] 4% (10/227 pages)
[=                             ] 4% (11/227 pages)
--snip--
[============================= ] 97% (222/227 pages)
[============================= ] 98% (223/227 pages)
[============================= ] 98% (224/227 pages)
[============================= ] 99% (225/227 pages)
[============================= ] 99% (226/227 pages)
[==============================] 100% (227/227 pages)
Verify successful
Done in 2.810 seconds

```


#### Hello_World_Arcada: Select, compile, and upload the code 

This version plots the output on the tft screen on the badge.  It's similar to the pre-compiled UF2. 

After some inspection, it looks like the code provided doesn't quite work with the display on my EdgeBadge. It resulted in a line instead of a dot, and it also removed the text footer on the screen after starting inference.  So I adjusted the code and also made a PR to the Adafruit repo:

* https://github.com/codycollier/Adafruit_TFLite/commit/5dfa0a7a7a48d67dfe5207520273ef371d4807a3
* https://github.com/adafruit/Adafruit_TFLite/pull/5


```
ide: arduino ide -> File -> Examples -> Adafruit TensorFlow Lite
. select hello_world_arcada
. click the Upload button (arrow)
. observe
```

Arduino IDE output for writing to flash

```
Sketch uses 158856 bytes (31%) of program storage space. Maximum is 507904 bytes.
Device       : ATSAMD51x19
Version      : v1.1 [Arduino:XYZ] Jun 23 2019 17:44:35
Address      : 0x0
Pages        : 1024
Page Size    : 512 bytes
Total Size   : 512KB
Planes       : 1
Lock Regions : 32
Locked       : none
Security     : false
BOD          : false
BOR          : true
Write 162048 bytes to flash (317 pages)

[                              ] 0% (0/317 pages)
[=                             ] 5% (16/317 pages)
[==                            ] 7% (24/317 pages)
--snip--
[=======================       ] 78% (248/317 pages)
[========================      ] 80% (256/317 pages)
[========================      ] 83% (264/317 pages)
[=========================     ] 85% (272/317 pages)
[==========================    ] 88% (280/317 pages)
[===========================   ] 90% (288/317 pages)
[============================  ] 93% (296/317 pages)
[============================  ] 95% (304/317 pages)
[============================= ] 98% (312/317 pages)
[==============================] 100% (317/317 pages)
Done in 1.916 seconds
Verify 162048 bytes of flash

[=                             ] 3% (11/317 pages)
[=                             ] 3% (12/317 pages)
[=                             ] 4% (13/317 pages)
[=                             ] 4% (14/317 pages)
[=                             ] 4% (15/317 pages)
--snip--
[============================= ] 97% (310/317 pages)
[============================= ] 98% (311/317 pages)
[============================= ] 98% (312/317 pages)
[============================= ] 98% (313/317 pages)
[============================= ] 99% (314/317 pages)
[============================= ] 99% (315/317 pages)
[============================= ] 99% (316/317 pages)
[==============================] 100% (317/317 pages)
Verify successful
Done in 3.971 seconds
```



