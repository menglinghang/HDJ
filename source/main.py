import json
import numpy as np
import time
import urllib2

from SimpleCV import Display, Image



def get_center(img):
    temp = img
    for i in range(5):
        temp = temp.erode()
    temp.save('target2.jpg')
    blobs = temp.findBlobs().sortArea()
    center = blobs[0]
    # print 'center:',center.coordinates()
    return center.coordinates()


def get_imgBin(img):
    img.binarize()
    temp = img.binarize().invert().morphOpen()
    return temp


def emendation(img):
    return img



def get_score(point):
    # print point
    x_value = point[0]
    y_value = point[1]
    distance = np.sqrt((x_value - center[0]) ** 2 + (y_value - center[1]) ** 2)
    score = 0
    if distance <= 102.83:
        score = 10
    elif distance <= 206.04:
        score = 9
    elif distance <= 308.42:
        score = 8
    elif distance <= 412.31:
        score = 7
    elif distance <= 513.28:
        score = 6
    else:
        score = 5
    return score


# - -----------------------------------------\

img0=Image('demo.jpg')
disp = Display()
imgBin0 = get_imgBin(img0)
imgBin0 = emendation(imgBin0)
center = get_center(imgBin0)
img_list = []
score = ''
templet = imgBin0
for i in range(1, 11):
    img = Image('demo' + str(i) + '.jpg')
    img.save(disp)
    time.sleep(0.1)
    imgBin = get_imgBin(img)
    imgBin = emendation(imgBin)
    imgBin.save(disp)
    time.sleep(0.1)
    silhouette = (imgBin - templet).morphOpen()
    silhouette.save('target' + str(i) + '.jpg')
    blobs = silhouette.findBlobs()
    if (len(blobs) > 0):
        point = blobs.sortArea()[-1].coordinates()
        score = score + str(get_score(point)) + ','
    templet = imgBin
print score

data1 = {
    'data': [score]
}

url = r'http://localhost:8080/getstatistic'

req = urllib2.Request(url)
resp = urllib2.urlopen(req, json.dumps(data1))
print resp.read()
