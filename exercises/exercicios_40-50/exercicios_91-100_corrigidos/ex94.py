class Pessoa:
    nome = ""
    idade = None

    def __init__(self, nome_passado, idade_passada):
        self.nome = nome_passado
        self.idade = idade_passada

    def quem_e_mais_velho(pessoa1, pessoa2):
        if pessoa1.idade >  pessoa2.idade:
            print( pessoa1.nome + "e mais velho(a) do que " + str(pessoa2.nome))
        elif pessoa2.idade > pessoa1.idade:
            print( pessoa2.nome + "é mais velho(a) do que " + str(pessoa1.nome))
        else:
            print("Eles(a) tem a mesma idade")

Pessoa1 = Pessoa("Carlos ", 25 )
pessoa2 = Pessoa("Anny ", 20)

Pessoa.quem_e_mais_velho(Pessoa1, pessoa2)

