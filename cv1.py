import cv2
from os import listdir
import numpy as np
import shutil

lijst = listdir("./clr/")
lgr = [i for i in lijst if i.endswith(".jpg")]
ksize = (3, 3)
anchor = (-1, -1)
lgr.sort(key=lambda x: int(x.split(".")[0]))
lgr
n = 0
for input in lgr:
    n += 1
    im = cv2.imread("./clr/" + input, 1)
    imc = cv2.imread("./clr/"+input)
    frame_HSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    threshsv=cv2.inRange(frame_HSV, (0, 0, 200), (179, 255, 255));
    res=cv2.bitwise_and(imc,imc,mask = threshsv)
    edges = cv2.Canny(res, 100, 200)
    print cv2.imwrite("./free/"+input,edges)
    print n


