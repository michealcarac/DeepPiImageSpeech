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

Install Tensorflow 2.4:
```
pip3 uninstall tensorflow
```
It is okay if it does not find any pre installed packages
```
pip3 install https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0-rc2/tensorflow-2.4.0rc2-cp37-none-linux_armv7l.whl
```
## Wake Word Model




