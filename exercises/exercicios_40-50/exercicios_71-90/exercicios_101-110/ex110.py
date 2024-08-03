class Documento:
    titulo = None
    conteudo = None

    def __init__(self, titulo_passado, conteudo_passado):
        self.titulo = titulo_passado
        self.conteudo = conteudo_passado

class Livro(Documento):
    autor = None

    def add_info_livro(self, autor_passado):
        self.autor = autor_passado
 
 