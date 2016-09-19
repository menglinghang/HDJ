# -*- coding: utf-8 -*-
from SimpleCV import Camera, Display, Image, Color
import cv2
import numpy as np
import time

img = Image('demo.jpg')
disp = Display()
# 对图像进行二值化以及进行滤波
'''
imgBin=img.binarize().invert()
for i in range(10):
    imgBin=imgBin.morphOpen()
for i in range(2):
    imgBin=imgBin.erode()
imgBin.save(disp)
circles=imgBin.findCircle()
circles=circles.sortArea()
if len(circles)!=0:
    circles.draw(width=3)
imgBin_with_circle=imgBin.applyLayers()

center=circles[-1].coordinates()
print center
imgBin_with_circle[center[0],center[1]]=Color.RED
imgBin_with_circle.save('target.jpg')
time.sleep(2)
'''
# 对图像进行腐蚀操作，使得图像呈现唯一的圆
while not disp.isDone():
    imgBin = img.binarize().invert().morphOpen()
    for i in range(5):
        imgBin = imgBin.erode()
    circles = imgBin.findBlobs().sortArea()
    if len(circles) > 0:
        circles[0].draw(width=2)
        print circles[0].coordinates()
        center = circles[0].coordinates()
        imgBin[center[0], center[1]] = Color.RED
        imgBin.applyLayers()
        imgBin.save('target.jpg')
    imgBin.save(disp)
