numeros_impares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_numeros_impares = []

for numero in numeros_impares:
    if numero % 2 == 1:
        lista_numeros_impares.append(numero)
    
print(lista_numeros_impares)