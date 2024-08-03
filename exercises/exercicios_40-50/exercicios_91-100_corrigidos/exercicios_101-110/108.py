class Veiculo:
    def Quantidade_de_rodas(self):
        return "Quantidade de Rodas"

class Moto(Veiculo):
    def Quantidade_de_rodas(self):
        return "2 rodas"
    
class Carro(Veiculo):
    def Quantidade_de_rodas(self):
        return "4 rodas"

carro = Carro()
moto = Moto()

print("Carro tem " + carro.Quantidade_de_rodas())
print("Moto tem " + moto.Quantidade_de_rodas())