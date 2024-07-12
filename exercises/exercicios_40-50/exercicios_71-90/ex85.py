
lista_pessoas = [
    ('Maria', 20),
    ('Ana', 22),
    ('Lara', 24),
    ('Luiz', 29),
    ('Clara', 27),
    ('Sarah', 35),
    ('Gustavo', 30)
]


pessoas_por_idade = {}


for nome, idade in lista_pessoas:
    if idade in pessoas_por_idade:
        pessoas_por_idade[idade].append(nome)
    else:
        pessoas_por_idade[idade] = [nome]


print("Pessoas agrupadas por idade:")
for idade, nomes in pessoas_por_idade.items():
    print(f"Idade {idade}: {nomes}")