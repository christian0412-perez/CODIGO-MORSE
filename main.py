from cgi import test
import os
import tkinter
from tkinter import StringVar
import tkinter.font as tkFont
import cv2
import numpy as np
from clasificador import Clasificador
import errno, os, stat, shutil

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise


if os.path.exists("./dataset/test"):
    shutil.rmtree("./dataset/test", ignore_errors=False, onerror=handleRemoveReadonly)
os.mkdir('./dataset/test')
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
        cv2.imwrite(f'./dataset/test/recorte{contador}.png',recorte)
        contador=contador+1

img=cv2.imread('numeros2.jpg')
cv2.namedWindow('display')
cv2.setMouseCallback('display',dibujar)

while(True):
    img=cv2.imread('numeros2.jpg')
    if(interruptor==True):
        cv2.rectangle(img,(xI,yI),(xF,yF),(255,0,0),2)
    cv2.imshow('display',img)
    k=cv2.waitKey(1)&0xff
    if(k==27):
        break
cv2.destroyWindow('display')
window = tkinter.Tk()
window.geometry("350x170")
window.configure(background='#D7FF90')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

def importar():
    #import_file_path = filedialog.askopenfilename()
    clasificador.predictAll()

tkinter.Button(window,text="predecir",font=12,command=importar).place(x=80,y=30)
textPrediction=StringVar()
texto2 = tkinter.Label(window,textvariable=textPrediction,font=fontStyle,background='#D7FF90').place(x=80,y=70)
clasificador = Clasificador()
clasificador.train()

window.mainloop()