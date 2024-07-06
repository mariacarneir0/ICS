Lista_de_entrada = ["maçã", "banana", "cereja"]
elemento = "banana"

def verifica_se_elemento_existe(Lista_de_entrada, elemento):
    for palavra in Lista_de_entrada:
        if palavra == elemento:
            return True
        
    return False

print(verifica_se_elemento_existe(Lista_de_entrada, elemento))