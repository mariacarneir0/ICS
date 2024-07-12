
dicionario1 = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3'
}


dicionario2 = {
    'chave4': 'valor4',
    'chave5': 'valor5',
    'chave6': 'valor6'
}


dicionario_combinado = {**dicionario1, **dicionario2}

print("Dicionário combinado:")
print(dicionario_combinado)