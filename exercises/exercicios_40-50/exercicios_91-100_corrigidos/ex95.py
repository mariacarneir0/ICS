from Pessoa import  Pessoa

pessoa1 = Pessoa("Maria", " Clara ", 14, " estagiaria ", " Avenida Extremidade numeros 281")
pessoa2 = Pessoa("João ", "Gabriel ", 48 , " Programador ", " Avenida Patos de Minas numero 100")
pessoa3 = Pessoa("Regina ", "Eugenia ", 44 , " Tecnica em enfermagem ", "Rua dos Buritis numero 310")

lista = [pessoa1, pessoa2, pessoa3]

for pessoa in lista:
    print(pessoa.imprimir_dados_completos())
