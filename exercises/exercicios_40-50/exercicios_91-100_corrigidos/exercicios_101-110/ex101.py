class pessoa:
    def init(self,_nome,_idade):
        self.nome = _nome
        self.idade = _idade

class estudante(pessoa):
    escola = None
    serie = None
    frequencia = None

    def add_info_estudante(self, escola, serie, frequencia):
        self.escola = escola
        self.serie = serie
        self.frequencia = frequencia

    def retornar_informacoes(self):
        return self.nome + str(self.idade) + self.escola + self.serie + self.frequencia

Estudante = estudante(" Maria ", 14)
Estudante.add_info_estudante(" escola silva de alencar ", "9 ano ", " 21")
exibir_informacoes = Estudante.retornar_informacoes()
print(exibir_informacoes)
