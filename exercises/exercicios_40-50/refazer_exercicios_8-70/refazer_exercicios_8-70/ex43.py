lista_de_entrada =  [10,20,30,40,50]

def calcular_media(lista):
    if not lista: 
        return 0
    soma = sum(lista)
    media = soma / len(lista)
    return media

resultado = calcular_media(lista_de_entrada)
print(resultado)