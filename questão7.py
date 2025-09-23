import random
import string

def gerar_senha(tamanho=8):
    # caracteres possíveis: letras maiúsculas, minúsculas e números
    caracteres = string.ascii_letters + string.digits  
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
print("Sua senha é:", gerar_senha(12))