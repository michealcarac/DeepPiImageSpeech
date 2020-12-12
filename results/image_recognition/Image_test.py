import cv2
import tensorflow as tf
import numpy as np

classes = ['none', 'one', 'ten']

model = tf.keras.models.load_model('vgg16_model')
cap1 = cv2.VideoCapture(0)

picture = 1

while True:
    ret1, frame1 = cap1.read()
    cv2.imshow('frame1', frame1)

    key = cv2.waitKey(1) & 0xFF
    if ret1 and key == ord('p'):
        frame1 = np.expand_dims(frame1, axis=0)
        guess = np.argmax(model.predict(frame1))
        print(classes[guess])
        picture += 1
    elif key == ord('q'):
        cap1.release()
        cv2.destroyAllWindows()
        break
