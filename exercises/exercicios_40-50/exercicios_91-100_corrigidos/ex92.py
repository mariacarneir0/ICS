class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""
    endereco = ""

    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada
        self.endereco = endereco_passado

    def retorna_endeco(self):
        return self.endereco
    
pessoa = Pessoa("Maria", "Clara", 14, "estagiaria", "Avenida Extremidade numero 338")
print(pessoa.retorna_endeco())

#teste