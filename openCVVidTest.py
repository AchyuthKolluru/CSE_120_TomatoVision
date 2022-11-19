import numpy as np
import cv2 as cv

toggle = False
chuc = True

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
count = 0
while True:
    count = count + 1;
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    if count == 100:
        toggle = True
    if toggle:
        cv.rectangle(frame,(0,0),(720,720),(0,0,255),-1)
    # Display the resulting frame
    cv.putText(frame, "frame: {}".format(count), (0, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 3)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord(' '):
        toggle = False
        chuc = False


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()