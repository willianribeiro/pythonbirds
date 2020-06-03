class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(*filhos)

    def cumprimentar(self):
        return f'Oi, {id(self)}'


if __name__ == '__main__':
    pessoa = Pessoa()
    print(Pessoa.cumprimentar(pessoa))
    print(id(pessoa))
    print(pessoa.cumprimentar())
