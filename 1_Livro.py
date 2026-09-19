class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    def editar_titulo(self, novo_titulo):
        self.titulo = novo_titulo


    def mostrar_tudo(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("-" * 30)



livro1 = Livro("Traição de Capitu", "Machado de Assis", 1899)


print("Dados originais do livro:")
livro1.mostrar_tudo()


livro1.editar_titulo("Dom Casmurro: Memórias de um Sobrado")


print(" Dados após alteração:")
livro1.mostrar_tudo()