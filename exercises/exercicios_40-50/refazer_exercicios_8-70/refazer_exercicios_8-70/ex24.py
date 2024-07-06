def troca_valores(valor1, valor2):
    valor3 = valor1
    valor1 = valor2
    valor2 = valor3
    return valor1, valor2
resultado = troca_valores(200, 900)
print (resultado)