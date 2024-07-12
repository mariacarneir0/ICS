
pessoas = {
    'Maria': {
        'idade': 20,
        'cidade': 'São Paulo',
        'profissão': 'Engenheira'
    },
    'Ana': {
        'idade': 25,
        'cidade': 'Rio de Janeiro',
        'profissão': 'Designer'
    },
    'Cida': {
        'idade': 38,
        'cidade': 'Belo Horizonte',
        'profissão': 'Professora'
    },
    'Danielly': {
        'idade':35,
        'cidade': 'Buritizeiro',
        'profissão': 'Médica'
    },
    'Emanuelly': {
        'idade': 22,
        'cidade': 'Patos de Minas',
        'profissão': 'Advogada'
    }
}

for nome, info in pessoas.items():
    print(f"Nome: {nome}")
    for chave, valor in info.items():
        print(f"  {chave.capitalize()}: {valor}")
    print()