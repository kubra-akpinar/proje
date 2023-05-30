# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:34:32 2023

@author: kadpk
"""

import cv2
import pickle

width = 100
height =40
#onceki secili alanları carparkposa yukluyor ve tekrar actigimizda hatirliyor
try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)
except: 
     posList = []
     




def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
        
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
 #dikdortgen icine sag tik siler
     
    with open("CarParkPos", "wb") as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread("otopark.png")

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,0,0),2)
        #genişlik ve yükseklik belirleme, renk, kalınlık,
        
    #print("poslist", posList)

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mouseClick)
    cv2.waitKey(1)



