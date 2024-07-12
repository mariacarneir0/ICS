
produtos = {
    'arroz': 10.5,
    'feijão': 8.0,
    'macarrão': 5.75,
    'leite': 3.5,
    'café': 12.0,
    'açúcar': 4.25
}

def filtra_produtos_acima_de(dicionario, valor_minimo):
    produtos_filtrados = {produto: preco for produto, preco in dicionario.items() if preco > valor_minimo}
    return produtos_filtrados


valor_minimo = 8.0

produtos_filtrados = filtra_produtos_acima_de(produtos, valor_minimo)

print(f"Produtos com preço acima de R${valor_minimo}:")
for produto, preco in produtos_filtrados.items():
    print(f"{produto}: R${preco}")