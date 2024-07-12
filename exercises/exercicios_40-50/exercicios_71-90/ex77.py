paises = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Estados Unidos': 'Washington, D.C.',
    'Canadá': 'Ottawa',
    'França': 'Paris'
}


def conta_itens(dicionario):
    return len(dicionario)


numero_de_itens = conta_itens(paises)
print(f"O número de itens no dicionário é: {numero_de_itens}")