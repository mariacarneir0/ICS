class Pessoa:
    nome = 'Maria Clara '
    sobrenome = 'Carneiro'
    idade = 14
    endereço : 'Rua das Flores, 123, São Paulo, SP '
    


    def init(self, nome_passado, sobrenome_passado, idade_passada, endereço_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.endereço = endereço_passado

    def nova_profissao(self, nova_profissao):
        self.profissao = nova_profissao
        return self.profissao
    
    def novo_endereço(self, novo_endereço):
        self.endereço = novo_endereço
        return self.endereço

pessoa = Pessoa()
print(pessoa.novo_endereço)
print(Pessoa.endereço) 
