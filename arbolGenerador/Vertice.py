
class Vertice:

    list_aristas = []
    valor = 0
    peso = 0

    def __init__(self, valor,peso):
        self.valor = valor
        self.peso = peso

    def set_peso(self,peso):
        self.peso = peso

    
    def arista(self, vertice):
        aris = self.Arista(self.valor,vertice,self.peso)
        self.list_aristas.append(aris)
        aris.set_aristas(aris)

    class Arista:
        all_aristas =[]

        def __init__(self,inicio,final,peso):
            self.inicio = inicio
            self.final = final
            self.peso = peso

        def set_aristas(self,arsita):
            self.all_aristas.append(arsita)
