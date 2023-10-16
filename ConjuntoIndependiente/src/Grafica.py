
from Vertice import Vertice
from Arista import Arista

from re import split



class Grafica(){
    def __init__(self):
        

    def creaGrafica(self):
    
        with open("grafica.txt") as reader:
            contador = 1
            vertice[]=0
            for i in reader:
                if contador == 1:
                    datos = i.split(",")
                    for j in datos:
                        vertice[j] = Vertice(j)
                    contador++
                else:
                    
        
}