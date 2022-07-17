import cv2
import numpy as np

xI,yI,xF,yF=0,0,0,0
interruptor= False
contador=0
def dibujar(event,x,y,flags,param):
    global xI,yI,xF,yF,interruptor,img,contador

    if(event==cv2.EVENT_LBUTTONDOWN):
        xI,yI=x,y
        interruptor= False
    if(event==cv2.EVENT_LBUTTONUP):
        xF,yF=x,y
        interruptor= True
        recorte=img[yI:yF,xI:xF,:]
        cv2.resize(recorte,(100,100))
        cv2.imwrite(f'recorte{contador}.png',recorte)
        contador=contador+1

img=cv2.imread('alfabeto.png')
cv2.namedWindow('display')
cv2.setMouseCallback('display',dibujar)
while(True):
    img=cv2.imread('alfabeto.png')
    if(interruptor==True):
        cv2.rectangle(img,(xI,yI),(xF,yF),(255,0,0),2)
    cv2.imshow('display',img)
    k=cv2.waitKey(1)&0xff
    if(k==27):
        break
cv2.destroyAllWindows()