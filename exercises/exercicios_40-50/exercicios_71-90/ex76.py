
paises = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Estados Unidos': 'Washington, D.C.',
    'Canadá': 'Ottawa',
    'França': 'Paris'
}


def verifica_pais(dicionario, pais):
    if pais in dicionario:
        return f"O país {pais} está no dicionário."
    
    else:
        return f"O país {pais} não está no dicionário."


pais_a_verificar = 'Brasil'
resultado = verifica_pais(paises, pais_a_verificar)
print(resultado)

pais_a_verificar = 'Espanha'
resultado = verifica_pais(paises, pais_a_verificar)
print(resultado)