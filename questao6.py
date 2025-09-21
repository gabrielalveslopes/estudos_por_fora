import random as r

def girar_dado():
    return r.randint(1, 6)

def jogar_jogo():
    print("Bem-vindo ao jogo de dados!")
    input("Pressione Enter para girar o dado...")
    resultado = girar_dado()
    print(f"Você tirou um {resultado}!")


if __name__ == "__main__":
    jogar_jogo()

