from Grafica import Grafica
from Arbol import Arbol
from Vertice import Vertice
from Arista import Arista
import queue
import csv
import sys

def BFS(grafica, primer_nodo):
    arbol = Arbol(grafica.lista_nodos)
    arbol.lista[primer_nodo].visitado = True
    arbol.lista[primer_nodo].distancia = 0
    q = queue.Queue()
    q.put(arbol.lista[primer_nodo])
    #print("Aristas del primer nodo",arbol.lista[primer_nodo].list_aristas)
    pl = ""
    for i in arbol.lista:
        pl = pl+","+i
    pl= pl[1:]
    print(pl)
    while (not q.empty()):
        u = q.get()
        #print("Trabajando con u",u.valor)
        for v in u.list_aristas:
            if v.inicio == u.valor:
                #print("trabajando con",v.inicio,"-",v.final,":",v.peso)
                v2 = arbol.lista[v.final]
                if not v2.visitado:
                    v2.visitado = True
                    v2.distancia = u.distancia +1
                    v2.padre = u
                    #Este print imprime el reultado final
                    print(u.valor+","+v2.valor+":"+v.peso+": distancia =",v2.distancia)
                    q.put(v2)

               
def llenar_graf(args,n,graf,inicio,fin,peso):
    with open(args) as file:
        encabezado = file.readline()
        for i in encabezado.strip().split(","):
            n[i] = Vertice(i)
            graf.add_nodo(i,n[i])

        renglon = csv.reader(file)

        for j in renglon:
            inicio = j[0]
            fin = j[1].split(":")[0]
            peso = j[1].split(":")[1]
            arista = Arista(inicio,fin,peso)
            n[inicio].add_arista(fin,peso)
            #graf.add_Garista(arista)
            #print("Trabajando en el nodo",inicio)
            

        



def leer(args):
    with open(args,newline='') as file:
        spamreader = file.readline()
        #encabezado = .readline()
        #print ("encabezdo", spamreader)
        for row in file:
            print("linea",row)
            


if __name__=="__main__":
    n = {}
    myGrafica = Grafica()
    s = "1,2"
    n_inicio = 0
    n_fin = 0
    peso = 0
    fileName = sys.argv[1]

    

    llenar_graf(fileName,n,myGrafica,n_inicio,n_fin,peso)
    #leer('grafica.txt')
    #for i in n:
     #   print(n)
    BFS(myGrafica,myGrafica.lista_nodos["1"].valor)