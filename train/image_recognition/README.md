This section was provided by @cascioo (Owen Casciotti)

```
test.py
```
There are two booleans to change. 

One is load which decides if you want to load an old model or train a new one. 

The other is train which sets the model to either trainable or not.

```
Image_test.py
```
This goes on your Raspberry Pi along with the model generated with the script above. 

***Keep in mind that this script can either use VGG16 or MobileNetV2. These can be removed if you decide to just train. 
But they can be loaded if the boolean for load is true***
