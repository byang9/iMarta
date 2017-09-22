# iMarta
iMarta is a program that would help assist Marta employees detect fights and trash in real time. It combines the power of AI and the many Marta cameras to create a safer and cleaner environment for Marta riders.

## Prerequisites
```
Python 2.x or 3.x
https://www.python.org/downloads/
```
```
Clarifai Access Key
https://www.clarifai.com/developer/signup/
```
```
Installation & Configuration of Clarifai Package

FOR MAC
pip install clarifai --upgrade
$ clarifai config
CLARIFAI_API_KEY: []: YOUR API KEY HERE

FOR WINDOWS
C:\Python27>python.exe Scripts\clarifai config
CLARIFAI_API_KEY: []: YOUR API KEY
```
## Running Tests
To get started with the Clarifai API you have to follow the tutorial [here](https://clarifai-python.readthedocs.io/en/latest/tutorial/). Next you will have to train your Clarifai AI. Next you will have to edit the Python script to include your labels. Finally you are ready to run and test out your AI.
## The Technology
The technologies we used to develop iMarta consisted of [Clarifai](https://www.clarifai.com/), and Python's OpenCV. We developed the code in Python, and used OpenCV to control the laptop camera and send frames to Clarifai. To train our AI we took over 200 photos and ran it through Clarifai's training process before testing our model in the python script. In the end our product was able to detect fighting scenes and trash on the floor.
## The Team
Phuc Nguyen
[Bowen Yang](https://github.com/byang9)
[Benson Yang](https://github.com/byangschool)
Rachel Lilja
[James Nguyen](https://github.com/chamewin)

