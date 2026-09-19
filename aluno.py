class Aluno:
    def __init__(self, nome, matricula, nota1, nota2, nota3,nota4,nota5):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5

    def calcular_media(self):
        soma = self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5
        return soma / 5

    def verificar_aprovacao(self):
        media = self.calcular_media()
        return "Aprovado " if media >= 7.0 else "Reprovado "


    def mostrar_dados(self):
        print(f"\n Nome: {self.nome}")
        print(f" Matrícula: {self.matricula}")
        print(f" Notas: {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}, {self.nota5}")
        media = self.calcular_media()
        print(f" Média: {media:.1f}")
        print(f" Status: {self.verificar_aprovacao()}")
        print("-" * 40)
  
aluno1 = Aluno("Gabriel", "202607", 8.7, 8.0, 9.2, 10.0, 10.0)
aluno2 = Aluno("Lucas", "202629", 8.7, 9.0, 9.0, 10.0, 8.9)


print("=== DADOS DOS ALUNOS ===")
aluno1.mostrar_dados()
aluno2.mostrar_dados()


