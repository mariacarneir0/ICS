palavra = "kaiak"
inicio = 0
fim = len(palavra) -1

e_um_palindromo = True

while True:
    if inicio == len(palavra):
        break

    letra_inicio = palavra[inicio]
    letra_fim = palavra[fim]

    if letra_inicio != letra_fim:
        e_um_palindromo = False
        break

    inicio = inicio + 1
    fim = fim -1


if e_um_palindromo == True:
    print("A palavra e um palindromo")
else:
    print("Não e um palindromo")