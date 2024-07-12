def ordenar_dict_por_valores_crescente(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


dicionario = {'Ana': 3000, 'João': 2500, 'Maria': 4000, 'Pedro': 3500}

dicionario_ordenado = ordenar_dict_por_valores_crescente(dicionario)

print("Dicionário ordenado por valores (crescente):", dicionario_ordenado)