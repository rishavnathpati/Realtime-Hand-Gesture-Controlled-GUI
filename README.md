# Realtime-Hand-Gesture-Controlled-GUI
___________________________________________________________________________________________________________________________________________________________________

This project is an interesting conglomeration of ML, Tensorflow, opencv and a few other python libraries which lets you control your mouse and various other graphical inputs(like inreasing/decreasing volume, changing screen brightness, seeking to a particular point in a video etc), just by using your hands.

* It recognises what gesture you are trying to make, and carries out specific functions according to that gesture.

* For example, the most interesting of the lot is controlling the mouse, clicking and dragging around stuffs around the screen using your index finger(for moving the pointer) and thumb(for clicking and dragging).

* Other gestures include the use of index and middle finger to raise or lower systemwide master volume.

* And there are many more to come.

Come join me and help me out to further enhance this project.

## How to make it work in your PC

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

Now as far as mouseControl method is concerned here it goes:

TODO: Will be added later, requires not much change for proper functionality
