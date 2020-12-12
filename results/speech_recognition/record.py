import os

import wave #ExportAudio
import pyaudio #TakeInAudio
import librosa #ReadAudio
import python_speech_features #CalculateMFFCs

import time
import matplotlib.pyplot as plt
from math import ceil
import tensorflow as tf
import numpy as np

tf.compat.v1.enable_eager_execution() #We call this to establish a tf session

# Load Frozen Model
path = os.getcwd()+'/wake_words_model'
#print(path)
model = tf.keras.models.load_model(path)
#print(model)
model.summary()


# Pi Hat Config 
RESPEAKER_RATE = 16000 #Hz
RESPEAKER_CHANNELS = 1 # Originally 2 channel audio, slimmed to 1 channel for a 1D array of audio 
RESPEAKER_WIDTH = 2
RESPEAKER_INDEX = 2  # refer to input device id
CHUNK = 1024
RECORD_SECONDS = 1 # Change according to how many seconds to record for
WAVE_OUTPUT_FILENAME = "output.wav" #Temporary file name
WAVFILE = WAVE_OUTPUT_FILENAME #Clean up name

# Pyaudio
p = pyaudio.PyAudio() #To use pyaudio

wake_words = ['stop','yes','no','on','off','sheila','other'] #Our trained words IN ORDER
num_mfcc = 16  

def WWpredict(input_file):
    mfccs = calc_mfcc(input_file)
    audio = []
    audio.append(mfccs)
    audio = np.expand_dims(audio,axis=-1)
    prediction = model.predict(audio,steps =None)
    #print(prediction)
    confidence = .5 #Confidence of the model
    pindex = np.argmax(prediction)
    for words in wake_words:
        print(words,prediction[0][wake_words.index(words)])
    if prediction[0][pindex] > confidence:
        print(wake_words[pindex])

# Function: Create MFCC from given path
def calc_mfcc(path):
    # Load wavefile
    signal, fs = librosa.load(path, sr=RESPEAKER_RATE)
    # Create MFCCs from sound clip
    mfccs = python_speech_features.base.mfcc(signal, 
                                            samplerate=fs,
                                            winlen=.256, #Original: 0.256
                                            winstep=0.050,
                                            numcep=num_mfcc,
                                            nfilt=26,
                                            nfft=4096,
                                            preemph=0.0,
                                            ceplifter=0,
                                            appendEnergy=False,
                                            winfunc=np.hanning)
    return mfccs.transpose()

def record(): #This function will record 1 second of your voice every 1 second and will output a wav file that it will overwrite every second
    
    stream = p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            input_device_index=RESPEAKER_INDEX,)
 
    print("* recording")
 
    frames = []
    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)): #Had it as ceil() now is int()
        data = stream.read(CHUNK)
        frames.append(data)
 
    print("* done recording")

    stream.stop_stream()
    stream.close()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
while(True):
    record()
    WWpredict(WAVFILE)
