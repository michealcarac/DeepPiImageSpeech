| Name           | Format       | Target Framework | Target Device             |
| :------------- | :----------- | :--------------- | :------------------------ |
| `model.pb`     | Frozen       | TensorFlow       | Large-Scale/Cloud/Servers |
:                : GraphDef     :                  :                           :
| `model.tflite` | Fully        | TensorFlow Lite  | Mobile Devices            |
: *(<20 kB)*     : Quantized*   :                  :                           :
:                : TFLite Model :                  :                           :
| `model.cc`     | C Source     | TensorFlow Lite  | Microcontrollers          |
:                : File         : for              :                           :
:                :              : Microcontrollers :                           :

**Fully quantized implies that the model is **strictly int8** quantized
**including** the input(s) and output(s).*
