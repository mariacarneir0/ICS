def remover_funcionarios_salario_baixo(funcionarios, salario_minimo):
    funcionarios_para_remover = [funcionario for funcionario, salario in funcionarios.items() if salario < salario_minimo]
    
    for funcionario in funcionarios_para_remover:
        del funcionarios[funcionario]
    
    return funcionarios

funcionarios = {
    'Ana': 3000,
    'Vitor': 2500,
    'Maria': 4000,
    'Lucas': 3500
}

salario_minimo = 3000

funcionarios_filtrados = remover_funcionarios_salario_baixo(funcionarios, salario_minimo)

print("Funcionários filtrados:", funcionarios_filtrados)