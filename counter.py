# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:34:32 2023

@author: kadpk
"""

import cv2
import pickle
import numpy as np

def checkParkSpaces(imgg):
    spaceCounter=0
    
    for pos in posList:
        x, y  = pos
        
        img_crop = imgg[y: y + height, x:x + width]
        count = cv2.countNonZero(img_crop)
        
        print("count:", count)
        
        if count < 690:
            color = (0,255,0)
            spaceCounter += 1
         
        else:
            color = (0, 0, 255)
            
            
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color,2)
        #cv2.putText(img, str(count), (x,y+height-2), cv2.FONT_HERSHEY_PLAIN, 1, color, 2) 
        #kalinlik 2 boyut 4
    cv2.putText(img, f"Bos Alan: {spaceCounter}/{len(posList)}", (15,24), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 4)
        
width = 100
height =40

cap = cv2.VideoCapture("carPark2.mp4")
with open("CarParkPos", "rb") as f:
    posList= pickle.load(f)
    
while True:
    success, img = cap.read()
    
    #siyah beyaz
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #gereksiz detaylardan kurtulma, ilerideki trashold işlemleri için
    #3 e 3luk, sigması 1
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    
    #threshold işlemleri: araclar beyaz kalanlar siyah olacak
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 25 , 16)
    
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    #cizgiler belirginlesti, siyah ve beyazi kalinlastirmak iteration kalinlik belirler
    imgDilate = cv2.dilate(imgMedian, np.ones((3,3)), iterations = 1)
    #siyahlar bos beyazlar dolu
    
    
    checkParkSpaces(imgDilate)
    cv2.imshow("img", img)
    #cv2.imshow("img", imgGray)
    #cv2.imshow("img", imgBlur)
    #cv2.imshow("img", imgThreshold)
    #cv2.imshow("img", imgMedian)
    #cv2.imshow("img2", imgDilate)
    
    cv2.waitKey(10)


