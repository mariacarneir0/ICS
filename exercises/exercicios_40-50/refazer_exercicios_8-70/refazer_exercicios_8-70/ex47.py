lista_de_entrada =  [1,2,3,4,5]

for numero in range(len(lista_de_entrada)):
    numero_elevado_ao_quadrado = lista_de_entrada[numero]
    if numero_elevado_ao_quadrado % 2 == 1:
        print(numero_elevado_ao_quadrado * numero_elevado_ao_quadrado)