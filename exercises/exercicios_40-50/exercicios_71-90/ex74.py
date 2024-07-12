
paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa",
    "Austrália": "Camberra",
    "Alemanha": "Berlim",
    "Índia": "Nova Délhi",
    "África do Sul": "Pretória"
}

# Removendo um país do dicionário
pais_para_remover = "Japão"
if pais_para_remover in paises_capitais:
    del paises_capitais[pais_para_remover]

# Exibindo o dicionário atualizado
print(paises_capitais)