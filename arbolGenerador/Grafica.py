from Vertice import Vertice
from Arista import Arista 
class Grafica:
    lista_nodos = []
    list_aris = []
    def __init__(self):
        print("clase creada")
    def add_nodo(self,n):
        self.lista_nodos.append(n)
    def add_arista(self,a):
        self.list_aris.append(a)

if __name__=="__main__":
    n = {}
    myGrafica = Grafica()
    s = "1,2"
    n_inicio = 0
    n_fin = 0
    peso = 0

    for i in s.split(","):
        n[i] = Vertice(i)
        myGrafica.add_nodo(n)
    
    i = "1,2:4"

    #for i in linea: //Esta de mas
    n_inicio = i.split(",")[0]
    aux = i.split(",")[1]
    n_fin = aux.split(":")[0]
    peso = aux.split(":")[1]
    print("inicio es ",n_inicio,"Fin es",n_fin,"peso es",peso)
    arista = Arista(n_inicio,n_fin,peso)
    myGrafica.add_arista(arista)
    n[n_inicio].add_arista(n_fin,peso)

    primera_ln = ""

    for i in n:
        print("Valor del nodo",i)
        primera_ln = primera_ln+","+i
    
    print(primera_ln)

    for i in myGrafica.list_aris:
        print(i.inicio,",",i.final,":",i.peso)


    

    