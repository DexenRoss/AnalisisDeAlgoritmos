import pandas as pd
import numpy as np

#Leemos nuestro archivo txt o csv 
df = pd.read_csv('ordenado.txt', header=None)
elements = df.values 

#Creamos la funcion de busqueda binaria
# @param num - numero a buscar
# @param elementos - arreglo de elementos
def busqueda_Binaria(num,elementos):
    mid = 0
    contador=0
    min = df.columns[0]
    max = df.columns[-1]
   
    while(int((max - min))> 1):
        mid = int(np.floor((max + min)/2))
        print(contador,'.-min y max', min,max)
        if(elementos[0][mid]==mid):
            print('valor encontrado!!')   # Busqueda exitosa
            return mid
        if(mid<elementos[0][mid]): # Busca en la parte izquierda de elementos
            max = mid
        else:                      # Busca en la parte derecha de elementos 
            min = mid
        contador+=1
                            
    print('Valor no encontrado')
    return -1                       # Busqueda fallida
    
b_bin= busqueda_Binaria(3,elements)
print(b_bin)

    