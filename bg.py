import cv2
import numpy as np
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

from PIL import Image, ImageOps
img = cv2.imread('face.png')
segmentor = SelfiSegmentation()
img = segmentor.removeBG(img,(255,255,255))
cv2.imwrite("whitebg.png", img)
