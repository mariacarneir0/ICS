lista_de_entrada = [5, 3, 9, 1, 10,]

def acha_maior(Lista):
    maior = Lista[0]

    for numero in Lista:
        if numero > maior:
            maior = numero

    return maior

res = acha_maior(lista_de_entrada)
print(res)