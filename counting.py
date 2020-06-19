"""

********************************************************
Autor = @lexbonella -- https://github.com/alexbonella  *                      *  
Fecha = '19/06/2020'                                   * 
Nombre = Counting Objects with YOLOV3                  * 
******************************************************** 

"""

import pandas as pd 
import collections
import numpy as np 
import json
import ast

def Counting_objects(filename,threshold):
    
    file = open(filename ,'r') 
    all_string = file.read()
    
    batch_list=all_string.split('Enter Image Path:')
    
    prediction={
                    'Linea':batch_list
                 }
    df=pd.DataFrame(prediction)
    
    df=df.drop(index=0,axis=0)  
    df=df.reset_index()
    df=df.drop(columns='index')
    
    objeto='%'
    df['Presencia_Objeto']=df['Linea'].apply(lambda x : x.find(objeto))
    
    df.loc[df['Presencia_Objeto']==-1,'Objetos']='Sin deteccion'
    df.loc[df['Presencia_Objeto']!=-1,'Objetos']='Objetos detectados'
    
    df_detec=df[df['Presencia_Objeto']!=-1]
    df_detec=df_detec.reset_index()
    df_detec=df_detec.drop(columns='index')
    
    file_img=[]
    obj_det=[]



    for i in range(len(df_detec)):
        file_img.append(df_detec['Linea'][i].split('\n')[0].split(': Predicted in')[0].split('/')[-1])

        det_aux=[]

        for j in range(1,len(df_detec['Linea'][i].split('\n'))-1,1):

            det_aux.append(df_detec['Linea'][i].split('\n')[j])
        obj_det.append(det_aux)
        
    
    count=[]
    list_obj_final=[]
    for i in range(len(obj_det)):

        list_obj_ind=[]

        for j in range(len(obj_det[i])):

            if int(obj_det[i][j].split(':')[1].split('%')[0].strip()) > threshold :
                list_obj_ind.append(obj_det[i][j].split(':')[0].strip())

            else : 
                pass

        count.append(len(list_obj_ind))
        objetos=str(collections.Counter(list_obj_ind))
        list_obj_final.append(ast.literal_eval(objetos.replace("Counter(","").replace(")","")))
        
    
    # Final Dataframe 
    meta_img={
    'Name Image' : file_img,
    'Counting object' : list_obj_final,
    'Total counting' : count
    }

    df_meta=pd.DataFrame(meta_img)
    
    return df_meta
            
  
