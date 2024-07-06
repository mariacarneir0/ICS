Lista_de_entrada = ["Olá ", "mundo ", "Python", "!"]

def concatena(lista_de_entrada):
    total = ""
    for elemento in lista_de_entrada:
     total += elemento
    return total

resultado = concatena(Lista_de_entrada)
print(resultado)