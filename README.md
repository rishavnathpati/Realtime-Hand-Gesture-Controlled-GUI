# Realtime-Hand-Gesture-Controlled-GUI
__________________________________________________________________________________________________________________________________________________________________
### Visual Demo:
This visual demo is based on the old directory

<p align="center">
  <img src="https://user-images.githubusercontent.com/40483229/114586575-74043580-9ca2-11eb-8e04-5dd07e54a2bb.gif">
</p>

This project is an interesting conglomeration of ML, Tensorflow, opencv and a few other python libraries which lets you control your mouse and various other graphical inputs(like inreasing/decreasing volume, changing screen brightness, seeking to a particular point in a video etc), just by using your hands.

* It recognises what gesture you are trying to make, and carries out specific functions according to that gesture.

* For example, the most interesting of the lot is controlling the mouse, clicking and dragging around stuffs around the screen using your index finger(for moving the pointer) and thumb(for clicking and dragging).

* Other gestures include the use of index and middle finger to raise or lower systemwide master volume.

* And there are many more to come.

Come join me and help me out to further enhance this project.

# How to make it work in your PC

## Requirements
* mediapipe 0.8.1
* OpenCV 3.4.2 or Later
* Tensorflow 2.3.0 or Later<br>tf-nightly 2.5.0.dev or later (Only when creating a TFLite for an LSTM model)
* scikit-learn 0.23.2 or Later (Only if you want to display the confusion matrix) 
* matplotlib 3.3.2 or Later (Only if you want to display the confusion matrix)

Well Ive been developing for this in Linux for Linux. So windows users might be a little bummed. But no worries, most of this works perfectly fine on windows too, barring volume control which I will soon be working on the Windows version too.

So as far as the current situation is considered, here goes some of the things you need to tweak accourding to your convinience.

### In the MultithreadedWebcam.py file :-
Change the value of *scr* variable according to your convinience. If you have a working/good webcam in your PC, put *src=0*. But if you have a weak webcam, or dont have it at all, simply install an app called ip webcam from playstore, start its server(scroll down at the end of the app), connect both of your devices to your router, and enter the ip adress of your android phone in *src*.
If you're using mobile data, simply connect your pc to your mobile hotspot and again enter the ip adress in *src*. For example:
![image](https://user-images.githubusercontent.com/40483229/114570295-567b9f80-9c93-11eb-8d2c-fb02e473e09a.png)


```
# when connect via router, subject to change from router to router
class VideoCaptureThreading:
    def __init__(
            self,
            src="http://192.168.0.4:8080/video",  # Enter current the url from ip webcam or enter ) or 1 to use local pc webcam
            width=1280,
            height=720),
 ```
 ```
# when connect via mobile hotspot, subject to change from device to device
class VideoCaptureThreading:
    def __init__(
            self,
            src="http://192.168.136.209:8080/video",  # Enter current the url from ip webcam or enter ) or 1 to use local pc webcam
            width=1280,
            height=720),
 ```
### Now open the same url in your PC and you will be greeted with something like this:
![image](https://user-images.githubusercontent.com/40483229/114570788-be31ea80-9c93-11eb-95a3-7f668cda1975.png)

Now go to Advanced settings section and make these changes:
![image](https://user-images.githubusercontent.com/40483229/114571054-fafde180-9c93-11eb-8221-3264ea3f5063.png)


### In HandTrackingModule.py file :-
You may tinker with the detectionConfidence and trackingConfidence values. Ill say there are pretty fine, but feel free to make necessary changes. Value must be within 0.1-0.9.
```
class HandDetector:
    def __init__(self,
                 mode=False,
                 maxHands=2,
                 detectionConfidence=0.8,# You have the option to change these values from the GestureController.py too
                 trackConfidence=0.9):
```
We are almost there. Yaayyy!!!
### In GestureController.py file :-
Here we have various values to tweak with. Firstly enter your screen resolution in place of variable sx and sy.
```
prevTime = 0
currTime = 0
sx, sy = 1920, 1080
camx, camy = 1280, 720
pinchFlag = 0
```
Now for my friends using Linux, you will not have to change much regarding volumeControl method.

And for the ones using Windows, you may integrate similar command line inputs. More information [here](https://github.com/roblatour/setvol)

### I have updated the repo with a very interesting addition from [Kazuhito00](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe)

This new addition let's you train your model using your own hand(steps for training discussed in "Training")

The old working directory is marked as *OLD_FILES*

This new repository contains the following contents.
* The OLD_FILES repo
* Sample program
* Hand sign recognition model(TFLite)
* Finger gesture recognition model(TFLite)
* Learning data for hand sign recognition and notebook for learning
* Learning data for finger gesture recognition and notebook for learning
* Gesture Controller script(GestureControler.py)
* And a script which lets you run your webcam using multithreading, thus highly increasing performance(MultithreadedWebcam.py)

# Working Demo
Here's how to run the demo using your webcam.
```bash
python MainApplication.py
```

The following options can be specified when running the demo.
* --device<br>Specifying the camera device number (Default：0)
* --width<br>Width at the time of camera capture (Default：1280)#Change it according to your webcam resolution
* --height<br>Height at the time of camera capture (Default：720)
* --use_static_image_mode<br>Whether to use static_image_mode option for MediaPipe inference (Default：Unspecified)
* --min_detection_confidence<br>
Detection confidence threshold (Default：0.5)
* --min_tracking_confidence<br>
Tracking confidence threshold (Default：0.5)

# Directory
<pre>
│  app.py
│  keypoint_classification.ipynb
│  point_history_classification.ipynb
│  
├─model
│  ├─keypoint_classifier
│  │  │  keypoint.csv
│  │  │  keypoint_classifier.hdf5
│  │  │  keypoint_classifier.py
│  │  │  keypoint_classifier.tflite
│  │  └─ keypoint_classifier_label.csv
│  │          
│  └─point_history_classifier
│      │  point_history.csv
│      │  point_history_classifier.hdf5
│      │  point_history_classifier.py
│      │  point_history_classifier.tflite
│      └─ point_history_classifier_label.csv
│          
└─utils
    └─cvfpscalc.py
</pre>
### MainApplication.py
This is a sample program for inference.<br>
In addition, learning data (key points) for hand sign recognition,<br>
You can also collect training data (index finger coordinate history) for finger gesture recognition.

### model/keypoint_classifier
This directory stores files related to hand sign recognition.<br>
The following files are stored.
* Training data(keypoint.csv)
* Trained model(keypoint_classifier.tflite)
* Label data(keypoint_classifier_label.csv)
* Inference module(keypoint_classifier.py)
* Model training notebook script for hand sign recognition (keypoint_classification.ipynb)

### model/point_history_classifier
This directory stores files related to finger gesture recognition.<br>
The following files are stored.
* Training data(point_history.csv)
* Trained model(point_history_classifier.tflite)
* Label data(point_history_classifier_label.csv)
* Inference module(point_history_classifier.py)
* Model training notebook script for finger gesture recognition (point_history_classification.ipynb)

### utils/cvfpscalc.py
This is a module for FPS measurement.

# Training
Hand sign recognition and finger gesture recognition can add and change training data and retrain the model.

### Hand sign recognition training
#### 1.Learning data collection
Press "k" to enter the mode to save key points（displayed as 「MODE:Logging Key Point」）<br>
<img src="https://user-images.githubusercontent.com/37477845/102235423-aa6cb680-3f35-11eb-8ebd-5d823e211447.jpg" width="60%"><br><br>
If you press "0" to "9", the key points will be added to "model/keypoint_classifier/keypoint.csv" as shown below.<br>
1st column: Pressed number (used as class ID), 2nd and subsequent columns: Key point coordinates<br>
<img src="https://user-images.githubusercontent.com/37477845/102345725-28d26280-3fe1-11eb-9eeb-8c938e3f625b.png" width="80%"><br><br>
The key point coordinates are the ones that have undergone the following preprocessing up to ④.<br>
<img src="https://user-images.githubusercontent.com/37477845/102242918-ed328c80-3f3d-11eb-907c-61ba05678d54.png" width="80%">
<img src="https://user-images.githubusercontent.com/37477845/102244114-418a3c00-3f3f-11eb-8eef-f658e5aa2d0d.png" width="80%"><br><br>
In the initial state, three types of learning data are included: open hand (class ID: 0), close hand (class ID: 1), and pointing (class ID: 2).<br>
If necessary, add 3 or later, or delete the existing data of csv to prepare the training data.<br>
<img src="https://user-images.githubusercontent.com/37477845/102348846-d0519400-3fe5-11eb-8789-2e7daec65751.jpg" width="25%">　<img src="https://user-images.githubusercontent.com/37477845/102348855-d2b3ee00-3fe5-11eb-9c6d-b8924092a6d8.jpg" width="25%">　<img src="https://user-images.githubusercontent.com/37477845/102348861-d3e51b00-3fe5-11eb-8b07-adc08a48a760.jpg" width="25%">

#### 2.Model training
Open "[keypoint_classification.ipynb](keypoint_classification.ipynb)" in Jupyter Notebook and execute from top to bottom.<br>
To change the number of training data classes, change the value of "NUM_CLASSES = 3" <br>and modify the label of "model/keypoint_classifier/keypoint_classifier_label.csv" as appropriate.<br><br>

#### X.Model structure
The image of the model prepared in "[keypoint_classification.ipynb](keypoint_classification.ipynb)" is as follows.
<img src="https://user-images.githubusercontent.com/37477845/102246723-69c76a00-3f42-11eb-8a4b-7c6b032b7e71.png" width="50%"><br><br>

### Finger gesture recognition training
#### 1.Learning data collection
Press "h" to enter the mode to save the history of fingertip coordinates (displayed as "MODE:Logging Point History").<br>
<img src="https://user-images.githubusercontent.com/37477845/102249074-4d78fc80-3f45-11eb-9c1b-3eb975798871.jpg" width="60%"><br><br>
If you press "0" to "9", the key points will be added to "model/point_history_classifier/point_history.csv" as shown below.<br>
1st column: Pressed number (used as class ID), 2nd and subsequent columns: Coordinate history<br>
<img src="https://user-images.githubusercontent.com/37477845/102345850-54ede380-3fe1-11eb-8d04-88e351445898.png" width="80%"><br><br>
The key point coordinates are the ones that have undergone the following preprocessing up to ④.<br>
<img src="https://user-images.githubusercontent.com/37477845/102244148-49e27700-3f3f-11eb-82e2-fc7de42b30fc.png" width="80%"><br><br>
In the initial state, 4 types of learning data are included: stationary (class ID: 0), clockwise (class ID: 1), counterclockwise (class ID: 2), and moving (class ID: 4). <br>
If necessary, add 5 or later, or delete the existing data of csv to prepare the training data.<br>
<img src="https://user-images.githubusercontent.com/37477845/102350939-02b0c080-3fe9-11eb-94d8-54a3decdeebc.jpg" width="20%">　<img src="https://user-images.githubusercontent.com/37477845/102350945-05131a80-3fe9-11eb-904c-a1ec573a5c7d.jpg" width="20%">　<img src="https://user-images.githubusercontent.com/37477845/102350951-06444780-3fe9-11eb-98cc-91e352edc23c.jpg" width="20%">　<img src="https://user-images.githubusercontent.com/37477845/102350942-047a8400-3fe9-11eb-9103-dbf383e67bf5.jpg" width="20%">

#### 2.Model training
Open "[point_history_classification.ipynb](model/point_history_classifier/point_history_classification.ipynb)" in Jupyter Notebook and execute from top to bottom.<br>
To change the number of training data classes, change the value of "NUM_CLASSES = 4" and <br>modify the label of "model/point_history_classifier/point_history_classifier_label.csv" as appropriate. <br><br>

#### X.Model structure
The image of the model prepared in "[point_history_classification.ipynb](point_history_classification.ipynb)" is as follows.
<img src="https://user-images.githubusercontent.com/37477845/102246771-7481ff00-3f42-11eb-8ddf-9e3cc30c5816.png" width="50%"><br>
The model using "LSTM" is as follows. <br>Please change "use_lstm = False" to "True" when using (tf-nightly required (as of 2020/12/16))<br>
<img src="https://user-images.githubusercontent.com/37477845/102246817-8368b180-3f42-11eb-9851-23a7b12467aa.png" width="60%">

# Reference
* [MediaPipe](https://mediapipe.dev/)
* [Kazuhito Takahashi](https://twitter.com/KzhtTkhs)
* [Codacus](https://thecodacus.com/2017/08/16/gesture-recognition-virtual-mouse-using-opencv-python/)

# Author
* [Rishav Nath Pati](https://github.com/rishavnathpati)
* [Kazuhito Takahashi](https://twitter.com/KzhtTkhs)

# Translation and other improvements
* [Nikita Kiselov](https://github.com/kinivi)
<<<<<<< HEAD
* [Rishav Nath Pati](https://github.com/rishavnathpati)
=======
* [Rishav Nath Pati](https://github.com/rishavnathpati)
>>>>>>> b9576c4aa3e8bea4e08498790f9fceb516942853
