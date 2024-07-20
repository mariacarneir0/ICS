class Pessoa:

    nome = ''
    quantidade = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.quantidade += 1 
    
    def quantidade_pessoas():
        return Pessoa.quantidade

pessoa1 = Pessoa("Ana")
pessoa2 = Pessoa("Clara")
pessoa3 = Pessoa("Luiz")

print(Pessoa.quantidade_pessoas())