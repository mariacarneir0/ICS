
dicionario_categorias = {
    'frutas': ['maçã', 'banana', 'ameixa', 'uva', 'morango'],
    'vegetais': ['cenoura', 'repolho', 'abobrinha', 'tomate', 'alface'],
    'bebidas': ['água', 'café', 'suco de laranja', 'refrigerante']
}


for categoria, itens in dicionario_categorias.items():
    print(f"{categoria.capitalize()}:")
    for item in itens:
        print(f" - {item}")
    print()