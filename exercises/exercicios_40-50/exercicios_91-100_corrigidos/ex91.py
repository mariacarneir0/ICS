class Pessoa:
    nome = ''
    sobrenome = ''
    idade = None
    profissao = ""


    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada

    def modifica_profissao(self, nova_profissao):
        self.profissao = nova_profissao

pessoa = Pessoa("Maria Clara", "Carneiro", 14, "estagiaria")
pessoa.modifica_profissao("Advogada")
print(pessoa.profissao)