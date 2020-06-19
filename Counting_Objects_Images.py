
"""

********************************************************
Autor = @lexbonella -- https://github.com/alexbonella  *                      *  
Fecha = '19/06/2020'                                   * 
Nombre = Counting Objects with YOLOV3                  * 
******************************************************** 

"""


import counting


filename = 'resultados_50_imgs_yolo.txt'
threshold = 30

detections=counting.Counting_objects(filename,threshold)
print(detections)