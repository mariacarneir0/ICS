def calcular_media_notas(estudantes):
    medias = {}
    
    for estudante, materias in estudantes.items():
        notas = materias.values()
        media = sum(notas) / len(notas)
        medias[estudante] = media
        
    return medias

# Exemplo de uso:
estudantes = {
    'Ana': {'Matemática': 8.5, 'Português': 7.5, 'História': 6.0},
    'Maria': {'Matemática': 9.0, 'Português': 8.0, 'História': 7.5},
    'Katia': {'Matemática': 7.0, 'Português': 6.5, 'História': 8.0}
}


