class Pessoa :
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def apresentacao(self):
        print(f"O nome da pessoa consultada é {self.nome}; \n A idade dele(a) é: {self.idade};")

    def fazer_aniversario(self):
        self.idade +=1 
        print(f"Feliz aniversário, {self.nome}!!! sua nova idade agora é: {self.idade}.")

pessoa1 = Pessoa("João Paulo", 30, 55, 1.60)
pessoa2 = Pessoa("Maria Laura", 25, 70, 1.80)

pessoa1.apresentacao()
pessoa1.fazer_aniversario()