lista_palavras = ["eu moro em Buritizeiro"]

for item in range(len(lista_palavras)):
    lista_palavras[item] = lista_palavras[item].replace("Buritizeiro", "São Romão")
    
print(lista_palavras)

#replace é uma função de string em Python que permite substituir todas as ocorrências de uma substring (parte da string) por outra substring