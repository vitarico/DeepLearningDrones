# 1, 2, 3 or 4
The approach takes frames of the camera feed and evaluates the class of the image using the pre-trained caffemodul within in the "test" folder. We based our classification algorithm for the camera pictures on four different states: 
0 = Goal straight ahead (the whole frame is visible), 1= goal to the right (right vertical and a bit of the horizontal bar visible), 2=goal to the left and 3= no goal in sight.
Our greatest challenge was to train a network, so that it can recognize these different stages independent of the goal size in the frame (distance to the goal) and independent of the background and light conditions.Depending on the classification the drone then flies ahead, turns right, turns left or keeps turning to find a goal. 
# Usage 
We used docker as a virtual box to execute the code, as we did not want to install cafe on our devices. Install docker and run it on windows via 
```
docker run -it -v $path to your directory$:/data/ mjdev/cdtm-deep-learning-drones /bin/bash
```
all the files in your directory should then be accessible in the data folder within docker. The caffemodul was unfortunatly too big to import it in github, so please download the "test" folder via this link:
````
https://drive.google.com/drive/folders/0ByM661MWi_eRb1NSZVRUTTFKQm8?usp=sharing
````
and store it in your directory. Put the control.py and test folder in the same directory, connect to the drone, run the control.py and press space to start the drone. The drone flies completely autonomous so there are only to input options:
Key | Action
----- | -----
space | start/land the drone
Our steering algorithm is then programed to keep the drone on a constant height above the ground and steer it according to the classification result of the current video frame of the drone’s front camera. If the classification returns 0 as most probable state, the drone will fly forward for a certain amount of time, when the most probable state is 1 or 2, it turns a little bit to the right or left, and it will turn right on state 3. After the commands are generated they are sent and executed on the drone via the ps_drone library. 
As we execute the program in docker, there is not a video feed, however for every picture that gets evaluated you get feedback on the console to what percentage the picture got classified in which class. As we trained the drone on goals with red and white striped barrier-tape, you will have to prepare the goals in a similar way for the program to work. 
# Background
We trained the neural network AlexNet with 6000 pictures of the different classes to create a simple, but robust finite state approach to achieve a completely autonomous navigation of the drone through the three goals.
