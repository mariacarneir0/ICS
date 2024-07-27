class Pessoa:

    nome = ''
    quantidade = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1 
    
    def quantidade_pessoas():
        return Pessoa.quantidade

pessoa1 = Pessoa("Laura")
pessoa2 = Pessoa("Cirilo")
pessoa3 = Pessoa("Julia mix")

print(Pessoa.quantidade_pessoas())