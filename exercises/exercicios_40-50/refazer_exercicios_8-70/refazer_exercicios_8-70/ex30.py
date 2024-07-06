numero1 = input("insira um numero: ")
numero2 = input("insira outro numero: ")

if int(numero2) < int(numero1):
    print(numero1 + " é menor que " + numero2)

elif int(numero1) < int(numero2):
    print(numero2 + " é maior que " + numero1)

else:
    print("Eles são iguais")