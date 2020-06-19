# Counting_Yolov3

En el siguiente repo se mostrara como realizar el conteo de objetos detectados en imagenes haciendo uso de Yolov3 

# Generalidades : 

Por lo general cuando necesitamos hacer conteo de objetos detectados en un lote de imagenes nos damos cuenta que no es tan sencillo como parece y ni hablar de conteo en videos , por tal motivo se creo este repo para abordar el conteo en imagenes. 

Inicialmente cuando realizamos el siguiente comando  para obtener las predicciones de una imagen con yolov3 : 

* `./darknet detect cfg/yolov3.cfg yolov3.weights /PATH/image.jpg`

Obtenemos la siguiente pantalla : 

![Screenshot (217)](https://user-images.githubusercontent.com/45697319/85161447-61a5a080-b225-11ea-903b-ef0dbc2ddc61.png)


Finalmente lo que vamos a hacer es tomar cada una de las detecciones en cada imagen y extraer esos datos para crear un **`Dataframe`** que contenga tanto el conteo total de objetos  como el conteo por clases en cada imagen.


# Creación del archivo.txt con las detecciones de cada imagen 

* Ir al siguiente tutorial --- >>>  https://github.com/alexbonella/Counting_Yolov3/blob/master/YOLO_POR_LOTES_Tutorial.ipynb

# Conteo de objetos 

Para este paso ya debemos tener nuestro `archivo txt` ya creado en el paso anterior y luego editamos la linea que corresponde al nombre del archivo en el **`Counting_Objects_Images.py`** , finalmente ejecutamos: 

* `python Counting_Objects_Images.py`

Y como podemos observar ya tenemos nuestro `Dataframe` con nuestro conteo por imagen 

![Screenshot (219)](https://user-images.githubusercontent.com/45697319/85163044-df6aab80-b227-11ea-95b9-f225bdf4f616.png)






