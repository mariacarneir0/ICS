class Animal:
    def som(self):
        return "Som de animal"

class Gato(Animal):
    def som(self):
        return "Miau"

gato = Gato()
print(gato.som())