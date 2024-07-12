
paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa",
    "Austrália": "Camberra"
}

pais = input("Digite o nome de um país: ")

if pais in paises_capitais:
    print(f"A capital de {pais} é {paises_capitais[pais]}.")
else:
    print("País não encontrado no dicionário.")