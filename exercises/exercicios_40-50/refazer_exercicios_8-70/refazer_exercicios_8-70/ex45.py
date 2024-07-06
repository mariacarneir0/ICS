lista = ["sol", "lua", "sol", "estrela", "lua", "lua"]
contagem = {}
for item in lista:
    if item in contagem:
        contagem[item] += 1
    else:
        contagem[item] = 1

print(contagem)