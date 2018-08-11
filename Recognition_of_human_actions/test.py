import numpy as np
import cv2
import sys

if len(sys.argv) < 2:
    exit(0)

cap = cv2.VideoCapture(sys.argv[1].strip())

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(24) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()