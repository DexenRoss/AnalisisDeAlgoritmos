from Arista import Arista
class Vertice:

    list_aristas = []
    valor = 0
    esRaiz = False
    visitado = False
    padre = None
    distancia = 100

    def __init__(self, valor):
        self.valor = valor
    
    def add_arista(self, vertice,peso):
        aris = Arista(self.valor,vertice,peso)
        self.list_aristas.append(aris)
        #print("Entre al nodo",self.valor,"Con el vertice",vertice)
    

if __name__=="__main__":
    nodo = Vertice("4")
    print(nodo.valor)