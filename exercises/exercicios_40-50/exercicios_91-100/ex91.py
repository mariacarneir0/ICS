class Pessoa:
    nome = 'Maria Clara '
    sobrenome = 'Carneiro'
    idade = 14
    profissao = ""


    def init(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada

    def nova_profissao(self, nova_profissao):
        self.profissao = nova_profissao
        return self.profissao

pessoa = Pessoa()
print(pessoa.nova_profissao("Advogada"))
print(Pessoa.profissao)