#ACHTUNG Je nachdem welche Richtung gerade gefilmt wird muss Line 44 angepasst werden
# 0 Gerade aus
# 1 Tor Rechts
# 2 Tor Links
# 3 Kein Tor zu sehen

import glob

Richtung=3

if Richtung==0:
    R="front"
if Richtung==1:
    R="right"
if Richtung==2:
    R="left"
if Richtung==3:
    R="no"


textfile = open("Labelfile" + R + "_Location2.txt", "w")

filenames = glob.glob('1/*.png')
print filenames

for x in range(0,len(filenames),1):
        number = filenames[x][2:]
        print number
        #print type(cap)
        textfile.write(number + " " + Richtung.__str__() + "\n")

textfile.close()
exit()


