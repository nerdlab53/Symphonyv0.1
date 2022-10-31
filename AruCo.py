import cv2 as cv
from cv2 import aruco as aruco
import numpy as np
import os

def findarucomarkers(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, ids]

def augmentAruco(bbox, id, img, imgAug, drawID=True):
    tl = bbox[0][0][0], bbox[0][0][1]
    tr = bbox[0][1][0], bbox[0][1][1]
    br = bbox[0][2][0], bbox[0][2][1]
    bl = bbox[0][3][0], bbox[0][3][1]
    h, w, c = imgAug.shape
    pts1 = np.array([tl, tr, br, bl])
    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    matrix, _ = cv.findHomography(pts2, pts1)
    imgOut = cv.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))
    return imgOut


def main():
    cap = cv.VideoCapture(0)
    imgAug = cv.imread("test2.jpeg")
    while True:
        success, img = cap.read()
        findarucomarkers(img)
        arucoFound = findarucomarkers(img)
        if len(arucoFound[0]) != 0:
            for bbox, ids in zip(arucoFound[0], arucoFound[1]):
                img = augmentAruco(bbox, id, img, imgAug)

        cv.imshow("Image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
