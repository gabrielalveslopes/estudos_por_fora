class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Gênero: {self.genero}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros(self):
        for livro in self.livros:
            print(livro.exibir_informacoes())

    def buscar_por_autor(self, autor):
        return [livro for livro in self.livros if livro.autor.lower() == autor.lower()]
    

Livro1 = Livro("1984", "George Orwell", 1949, "Distopia")
Livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia")
Livro3 = Livro("Dom Casmurro", "Machado de Assis", 1899, "Romance")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(Livro1)
biblioteca.adicionar_livro(Livro2)
biblioteca.adicionar_livro(Livro3)
biblioteca.listar_livros()
resultados = biblioteca.buscar_por_autor(input("\nDigite o nome do autor para buscar seus livros: "))
print(f"\nLivros do autor {input}:")

for livro in resultados:
    print(livro.exibir_informacoes())
