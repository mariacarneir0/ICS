from django.shortcuts import render

def ex1(request):
    return render(request, 'ex1.html')

def ex2(request):
    data = {}
    if request.method == 'POST':
        valor1 = request.POST.get('valor1')
        valor2 = request.POST.get('valor2')
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex2.html', data)


def ex3(request):
    data = {}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f'Seu nome é {nome} e sua idade é {idade}'
        print(frase)
        data['frase'] = frase
    return render(request, 'ex3.html', data)
    

def ex4(request):
    data = {}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        soma = int(valor1) + int(valor2)
        data['soma'] = soma
    return render (request, 'ex4.html',data)

def ex5(request):
    data = {}
    if request.method == 'POST':
        palavra = request.POST.get('palavra')
        quantidade = f'{len(palavra)}'
        data['quantidade'] = quantidade 
    return render(request, 'ex5.html', data)

def ex6(request):
    data = {}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        palavra3 = request.POST.get("palavra3")
        palavra4 = request.POST.get("palavra4")
        palavra5 = request.POST.get("palavra5")
        frase = str(palavra1) + " " + str(palavra2) + " " + str(palavra3) + " " + str(palavra4) + " " + str(palavra5)
        data['frase'] = frase
    return render (request, 'ex6.html', data)

def ex7(request):
    data = {}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma
    return render (request, 'ex7.html', data)

def ex8(request):
    data = {}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + 1
        data['soma'] = soma
    return render (request, 'ex8.html', data)

def ex9(request):
    data = {}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        frase = f'Olá {nome}'
        data['frase'] = frase
    return render (request, 'ex9.html', data)

def ex10(request):
    data = {}
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma
    return render (request, 'ex10.html', data)

def ex11(request):
    data = {}
    if request.method == 'POST':
        palavra = request.POST.get("palavra") 
        if palavra:
            caracteres = len(palavra)
            data['caracteres'] = caracteres
        else:
            data['caracteres'] = 0  
    return render(request, 'ex11.html', data)

def ex12(request):
    data = {}
    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        parte3 = str(parte1) + " " + str(parte2)
        data['parte3'] = parte3
    return render (request, 'ex12.html', data)

def ex13(request):
    data = {}
    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex13.html', data)

def ex14(request):
    data = {}
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex14.html', data)

def ex15(request):
    data = {}
    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = str(frase) + ' ' + str(frase) + ' ' + str(frase)
        data['frase1'] = frase1
    return render(request, 'ex15.html', data)

def ex16(request):
    data = {}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex16.html', data)
    
def ex17(request):
    data = {}
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " " + str(palavra1) + " " 
        data['frase'] = frase
    return render (request, 'ex17.html', data)

def ex18(request):
    data = {}
    if request.method == 'POST':
        cidade1 = request.POST.get("cidade1")
        cidade2 = request.POST.get("cidade2")
        junçao = str(cidade1) + " " + str(cidade2) +  " "
        data['junçao'] = junçao
    return render (request, 'ex18.html', data)


def ex19(request):
    data = {}
    if request.method.get == 'POST':
     nome = request.GET.get('nome', '')
     saudaçao = input("Olá", nome)
     data['saudaçao'] = saudaçao
     return render (request, 'ex19.html', data)

def ex20(request):
    data = {}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex20.html', data)


