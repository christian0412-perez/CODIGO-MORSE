import os
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32,(3,3),input_shape=(30,30,1),activation=tf.nn.relu),
            tf.keras.layers.MaxPooling2D(2,2),

            tf.keras.layers.Conv2D(64,(3,3),activation=tf.nn.relu),
            tf.keras.layers.MaxPooling2D(2,2),

            tf.keras.layers.Conv2D(128,(3,3),activation=tf.nn.relu),
            tf.keras.layers.MaxPooling2D(2,2),

            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(4, activation=tf.nn.softmax) #para clasificacion
        ])

categorias = []
imagenes =[]
labels =[]
resultList={"imagen dada": [], "prediccion": []}
class Clasificador:


    def train(self):

        globals()["categorias"] = os.listdir('.\\dataset\\train\\')
        print(globals()["categorias"])
        x=0
        for category in globals()["categorias"]:
            for imagen in os.listdir('.\\dataset\\train\\'+category):
                print(imagen)
                img = Image.open('.\\dataset\\train\\'+category+"\\"+imagen).resize((30,30))
                img = np.asarray(img)
                print(img.shape)
                img_rgb = img[:,:,0]
                print(img_rgb.shape)
                globals()["imagenes"].append(img_rgb)
                globals()["labels"].append(x)
            x+=1
        globals()["imagenes"] = np.asanyarray(globals()["imagenes"])
        globals()["labels"] = np.asarray(globals()["labels"])
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        historial = model.fit(globals()["imagenes"],globals()["labels"],epochs=100)
        plt.xlabel('# Epochs')
        plt.ylabel("loss")
        plt.plot(historial.history["loss"])
        plt.show()
    def predictAll(self):
        y=[]
        
        for category in globals()["categorias"]:
            for imagen in os.listdir('.\\dataset\\train\\'+category):
                img = Image.open('.\\dataset\\train\\'+category+"\\"+imagen).resize((30,30))
                img = np.asarray(img)
                
                img_rgb = img[:,:,0]
                print(img_rgb.shape)
                img_rgb = np.array([img_rgb])
                predicciones = model.predict(img_rgb)
                y.append(np.argmax(predicciones[0]))
                prediccion= categorias[np.argmax(predicciones[0])]
                print("archivo dado : ", imagen)
                print("prediccion de la red: ",categorias[np.argmax(predicciones[0])])
                resultList["imagen dada"].append(imagen)
                resultList["prediccion"].append(y)
        y=np.asanyarray(y)
        yP= y[:]
        df =    pd.DataFrame(resultList)
        print(globals()["labels"])
        print(yP)

        df.to_csv('./output.csv')    
        matriz = tf.math.confusion_matrix(globals()["labels"],yP)
        figMatriz= plt.figure(figsize=(6,6))
        sns.heatmap(matriz,xticklabels=globals()["categorias"],yticklabels=globals()["categorias"],annot=True,fmt="g",cmap="mako")
        plt.xlabel("prediccion")
        plt.ylabel("Label")
        plt.show()
    def predict(self):
        y=[]
        stringSalida=''
        for imagen in os.listdir('.\\dataset\\test\\'):
            img = Image.open('.\\dataset\\test\\'+imagen).resize((30,30))
            img = np.asarray(img)
            
            img_rgb = img[:,:,0]
            print(img_rgb.shape)
            img_rgb = np.array([img_rgb])
            predicciones = model.predict(img_rgb)
            y.append(np.argmax(predicciones[0]))
            prediccion= categorias[np.argmax(predicciones[0])]
            print("archivo dado : ", imagen)
            print("prediccion de la red: ",categorias[np.argmax(predicciones[0])])
            resultList["imagen dada"].append(imagen)
            resultList["prediccion"].append(prediccion)
            if(prediccion=="punto"):
                stringSalida = stringSalida+"."
            if(prediccion=="raya"):
                stringSalida = stringSalida+"-"
            if(prediccion=="diagonal"):
                stringSalida = stringSalida+"/"
            if(prediccion=="diagonal doble"):
                stringSalida = stringSalida+"//"

        y=np.asanyarray(y)
        yP= y[:]
        print(stringSalida)
        df =    pd.DataFrame(resultList)
        print(globals()["labels"])
        print(yP)
        df.to_csv('./output.csv')    
        return stringSalida

        #return(categorias[np.argmax(predicciones[0])])


