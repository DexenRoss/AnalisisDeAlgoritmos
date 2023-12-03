from Arista import Arista
class Vertice:

    list_aristas = []
    valor = 0

    def __init__(self, valor):
        self.valor = valor
    
    def add_arista(self, vertice,peso):
        aris = Arista(self.valor,vertice,peso)
        self.list_aristas.append(aris)

if __name__=="__main__":
    nodo = Vertice("4")
    print(nodo.valor)