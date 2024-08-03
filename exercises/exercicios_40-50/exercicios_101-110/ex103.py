class Carro:
    marca = None
    modelo = None

    def __init__(self, marca_passada, modelo_passado):
        self.marca = marca_passada
        self.modelo = modelo_passado

class CarroEletrico(Carro):
    autonomia = None

    def add_info_CarroEletrico(self, autonomia_passada):
        self.autonomia = autonomia_passada

    def detalhes(self):
        return self.marca + self.modelo + str(self.autonomia)
    
carro_eletrico = CarroEletrico("Gol", " Bolinha ")
carro_eletrico.add_info_CarroEletrico(615)
Detalhes = carro_eletrico.detalhes()
print(Detalhes)

        

