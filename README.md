# DeepPiImageSpeech
Speech Recognition and Image Recognition Deep Learning on Raspberry Pi Zero W

This entire project will be written in Python, so it would be beneficial to have a basic understanding of Python and have Python3 downloaded on your computer and Raspberry Pi

***Please read [InitialSetup](https://github.com/michealcarac/DeepPi/blob/main/InitialSetup.md) first if haven't already***

## Getting Started
**For this project, you will need a few things**
1. A computer to install some programs on
2. A internet connection
3. A way to create a MicroSD card for the Zero W with SSH or VNC albeit another Raspberry Pi, hooking up some peripherals to the Zero, or some other way.
4. Components listed [Here](https://docs.google.com/spreadsheets/d/1M7MrT1gzgztbvuXfkKRB7sXJfgQoq0oRnmKZJjNunso/edit?usp=sharing)

**The following programs that will be used**
1. Google Colab
3. Tensorflow
4. Python3
5. OpenCV

**Now, only some of these programs will be needed on your Computer and some on your Raspberry Pi:**

**Computer:**
1. Google Colab
2. Tensorflow

**Raspberry Pi Zero W:**
1. Tensorflow
2. OpenCV
4. Python3

## Wake Word Model
Set up Anaconda on your computer ---> 

First, install Tensorflow 1.15.2 on your Raspberry Pi
```
sudo apt-get update
sudo apt-get upgrade
pip uninstall tensorflow
pip3 uninstall tensorflow
sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
sudo apt-get install libatlas-base-dev libatlas3-base
pip3 install h5py==2.10.0
pip3 install -U --user six wheel mock
pip3 install https://github.com/Qengineering/Tensorflow-Raspberry-Pi/raw/master/tensorflow-1.15.2-cp37-cp37m-linux_armv7l.whl
```
Now check what version of python is on your Pi
```
python3 --version
```
Keep note of this version

Now on your computer, you want to create a Anaconda environment with that python version with the command:
```
conda create --name tf1.15.2 python=3.7.3 
```
Note: ```tf1.15.2``` is just a name I chose and ```3.7.3``` is the version of python on my Pi

Now we need to install Tensorflow 1.15.2 in that environment

Access the environment with 
```
conda activate tf1.15.2
```
Install Tensorflow 1.15.2:
```
conda install tensorflow=1.15.2
```




