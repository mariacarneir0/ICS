nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Você está aprovado com média", media)
elif 5 <= media < 7:
    print("Você está em recuperação com média", media)
else:
    print("Você está reprovado com média", media)