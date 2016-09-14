import libardrone.libardrone as libardrone
import cv2
import time
import os
import ps_drone

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    #  measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def dronestart():
    drone = ps_drone.Drone()  # Start using drone
    drone.startup()  # Connects to drone and starts subprocesses
    drone.printBlue("Connected to Drone")
    drone.reset()  # Always good, at start


    while drone.getBattery()[0] == -1:    time.sleep(0.1)  # Waits until the drone has done its reset
    time.sleep(0.5)  # Give it some time to fully awake

    drone.printBlue("Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1]))  # Gives a battery-status
    return drone


#ACHTUNG Je nachdem welche Richtung gerade gefilmt wird muss Line 44 angepasst werden
# 0 Gerade aus
# 1 Tor Rechts
# 2 Tor Links
# 3 Kein Tor zu sehen

Richtung=3

if Richtung==0:
    R="front"
if Richtung==1:
    R="right"
if Richtung==2:
    R="left"
if Richtung==3:
    R="no"



#initalisiere Drone Class
drone = libardrone.ARDrone(True)
#drone=drone=dronestart()
#drone.reset()
running=1
count=700
#os.mkdir(Richtung.__str__())

cap = drone.get_image()
#cap=drone.VideoImage
cap = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
cv2.imshow('Frame', cap)
textfile = open("Labelfile" + R + "_Location2.txt", "w")
time.sleep(4)

while running:

    cap = drone.get_image()
    cap= cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)
    #cap=drone.VideoImage

    # Check for Blurry
    gray = cv2.cvtColor(cap, cv2.COLOR_RGB2GRAY)
    fm = variance_of_laplacian(gray)
    print fm
    if fm < 30:
        print R + "%d.png" % count + "Was Blurry"
    else:
        cv2.imwrite(os.path.join(Richtung.__str__(),R + "%d.png" % count), cap)  # save frame as PNG file
        print 'Wrote File Number %d' % count

        # Schreibe Textdatei
        number = R + count.__str__() + ".png"
        print number
        #print type(cap)
        textfile.write(number + " " + Richtung.__str__() + "\n")
        count += 1


    time.sleep(0.3)

    if cv2.waitKey(1) & 0xFF == 27:  # escape key pressed
        textfile.close()
        running =0
        exit()
