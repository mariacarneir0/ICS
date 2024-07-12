
paises = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Estados Unidos': 'Washington, D.C.',
    'Canadá': 'Ottawa',
    'França': 'Paris'
}

def atualiza_capital(dicionario, pais, nova_capital):
    if pais in dicionario:
        dicionario[pais] = nova_capital
        return f"A capital do {pais} foi atualizada para {nova_capital}."
    else:
        return f"O país {pais} não está no dicionário."

