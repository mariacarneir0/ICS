class InstrumentoMusical:
    def tocar(self):
        return "Som de Instrumento"

class Guitarra(InstrumentoMusical):
    def tocar(self):
        return "Tocando Guitarra"

Toca_guitarra = Guitarra()
print(Toca_guitarra.tocar())