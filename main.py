from cgi import test
import os
import tkinter
from tkinter import StringVar
from tkinter import filedialog
import tkinter.font as tkFont
import cv2
import numpy as np
from clasificador import Clasificador
import errno, os, stat, shutil
from traductor import Traductor
import re
from PIL import Image
import cv2
from pytesseract import *
window = tkinter.Tk()
window.geometry("350x170")
window.configure(background='#D7FF90')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
cv2.namedWindow('display')

def importar():
    #import_file_path = filedialog.askopenfilename()
    clasificador.predictAll()
    
def importar2():
    import_file_path = filedialog.askopenfilename()
    clasificador.predict()
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img=cv2.imread(import_file_path)
    cv2.imshow('display',img)
    resultado = pytesseract.image_to_string(img,lang='equ')
    print(resultado)
    newChain=resultado.replace("−","-")
    newChain=newChain.replace("∕","/")
    newChain=newChain.replace("⋅",".")
    newChain=newChain.replace("∙",".")
    newChain=newChain.replace("∣","/")
    newChain2=re.sub(r"\s+", "", newChain)
    print(newChain2)
    traducido=traductor.traducir(newChain2)
    print(traducido)
    textPrediction.set(traducido)
tkinter.Button(window,text="matriz de confusion",font=12,command=importar).place(x=80,y=30)
textPrediction=StringVar()
texto2 = tkinter.Label(window,textvariable=textPrediction,font=fontStyle,background='#D7FF90').place(x=80,y=110)
tkinter.Button(window,text="importar y predecir",font=12,command=importar2).place(x=80,y=70)
clasificador = Clasificador()
traductor = Traductor()
clasificador.train()

window.mainloop()