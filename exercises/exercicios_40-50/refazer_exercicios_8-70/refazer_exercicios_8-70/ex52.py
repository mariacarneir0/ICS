temperaturas = [23, 20, 19, 22, 30, 25]
menor_temperatura = temperaturas[0]
maior_temperatura = temperaturas[0]

for numero in temperaturas:
    if menor_temperatura > numero:
        menor_temperatura = numero
    if maior_temperatura < numero:
        maior_temperatura = numero

print(f"A maior temperatura é {maior_temperatura}")
print(f"A menor temperatura é {menor_temperatura}")