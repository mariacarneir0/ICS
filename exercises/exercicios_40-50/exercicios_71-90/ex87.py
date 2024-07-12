
notas_alunos = {
    'Alice': 9.5,
    'Bruna': 7.2,
    'Cida': 5.8,
    'Daniella': 6.5,
    'Eliane': 8.9
}

tabela_conversao = {
    (9.0, 10.0): 'A',
    (8.0, 9.0): 'B',
    (7.0, 8.0): 'C',
    (6.0, 7.0): 'D',
    (0.0, 6.0): 'F'
    
}

def converter_notas_para_conceitos(notas, tabela):
    conceitos = {}
    for aluno, nota in notas.items():
        for faixa, conceito in tabela.items():
            if faixa[0] <= nota < faixa[1]:
                conceitos[aluno] = conceito
                break  
    return conceitos


conceitos_alunos = converter_notas_para_conceitos(notas_alunos, tabela_conversao)



print("Conceitos dos alunos:")
for aluno, conceito in conceitos_alunos.items():
    print(f"{aluno}: {conceito}")