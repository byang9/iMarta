import numpy as np
import cv2
import time
from clarifai.rest import ClarifaiApp
import json
import os
import subprocess

app = ClarifaiApp()
model = app.models.get('ride')
label1 = 'punching'
label2 = 'trash'
label3 = 'nPunching'
counter = 1
firstFrame = True
recording = False #if fight breaks out
trashFound = False #if trash is seen
printout = {}
vidWidth = 640
vidHeight = 480

os.remove('recording.m4v')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('recording.m4v',fourcc,5.0,(vidWidth,vidHeight))
try:
    while(True):
        #capture frame-frame
        ret, frame = cap.read()
        
        #lower resolution to 320x240 and save frame
        ret = cap.set(3,vidWidth)
        ret = cap.set(4,vidHeight)
        cv2.imwrite('frame.jpg',frame)

        #Display the frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #calling Clarifai API and printout in a readable fashion
        if recording == False and trashFound == False:
            response = model.predict_by_filename('frame.jpg')
            for output in response['outputs'][0]['data']['concepts']:
                if output['name'] == label1:
                    printout[label1] = output['value']
                    if(output['value']> 0.3):
                        recording = True
                elif output['name'] == label3:
                    printout[label3] = output['value']
                else:
                    printout[label2] = output['value']
                    if(output['value']>0.65 and firstFrame == False):
                        trashFound = True
            
            if(printout[label1] - printout[label3] > 0.25 and firstFrame == False):
                recording = True
            print(printout)
        if counter <50 and (recording == True ):#or trashFound == True):
            counter += 1
            print("recording")
            #create videowriter object
            out.write(frame)
        elif recording == True or trashFound == True:
            print ("Shutting down")
            #release at end
            cap.release()
            cv2.destroyAllWindows
            out.release()
            break
        firstFrame = False
except KeyboardInterrupt:
    print ("Shutting down")
    #release at end
    cap.release()
    cv2.destroyAllWindows
    out.release()

if recording == True:
    #Popup box saying video recorded
    applescript = """
    display dialog "Fighting has been detected on Red Train - Cart 9. Arriving at 6:40pm, on southbound rail. Please check video feed for more information" ¬
    with title "Alert to Five Points Marta Station" ¬
    with icon caution ¬
    buttons {"OK"}
    """
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)
elif trashFound == True:
    #Popup box saying trash found
    applescript = """
    display dialog "Trash has been detected on Red Train - Cart 7. Arriving at 6:40pm, on southbound rail. Please check picture for more information" ¬
    with title "Alert to Five Points Marta Station" ¬
    with icon caution ¬
    buttons {"OK"}
    """
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)
