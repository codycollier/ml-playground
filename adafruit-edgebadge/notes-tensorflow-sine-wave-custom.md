

## Notes on customizing TensorFlow Sine Wave Demo

#### References

* https://learn.adafruit.com/tensorflow-lite-for-edgebadge-kit-quickstart/customized-wave-demo
* https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/train/train_hello_world_model.ipynb


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


#### Customize the model

Make your own sine wave data

```
recreate the data
. open the collab notebook
. read and run everything
. copy output data and replace in sine_model_data.h
. recompile and write to flash
. observe
```


Make data for a different wave form  
(train model on different data generated from different function)

```
customize the model
. open the collab notebook and make a copy somewhere
. adjust generating function and misc params like skip
    . tried out tanh, cosine, -cos, -sin
    . chose -sin
. generate more data
. replace and re-write
. observe
```



