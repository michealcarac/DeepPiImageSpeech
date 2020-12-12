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
1. Jupyter Notebook
2. Anaconda
3. Tensorflow (Match version with Pi)
4. Python3 (Match version with Pi)
5. OpenCV2

**Now, only some of these programs will be needed on your Computer and some on your Raspberry Pi:**

**Computer:**
1. Tensorflow 1.15.2
2. Anaconda
3. Python
4. Jupyter Notebook

**Raspberry Pi:**
1. Tensorflow 1.15.2
2. OpenCV2
3. Python3

## Wake Word Model (TODO: Move contents to initialsetup)
Set up Anaconda on your computer ---> [Here](https://docs.anaconda.com/anaconda/install/)

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
pip3 install tensorflow==1.15.2
```
If you want to train with gpu, install ```tensorflow-gpu==1.15.2```

Install OpenCV in your environment with
```
pip3 install opencv-python
```
Do this on your Pi as well. 

Now, you should be able to run our programs with no issues. The notebooks plus the Remove Files Script is for your Computer and the other python scripts are for the Raspberry Pi. We are using Googles Speech Dataset and VGG16 Dataset for Image Recognition which we transfer learned with our own images and classes. 




