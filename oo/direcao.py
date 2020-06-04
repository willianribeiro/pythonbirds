class Direcao:
    COMPASS = ['Norte', 'Leste', 'Sul', 'Oeste']

    def __init__(self):
        self.valor = "Norte"

    def girar_a_direita(self):
        current_index = self.COMPASS.index(self.valor)
        new_index = current_index + 1
        if new_index > 3:
            new_index = 0
        self.valor = self.COMPASS[new_index]

    def girar_a_esquerda(self):
        current_index = self.COMPASS.index(self.valor)
        new_index = current_index - 1
        if new_index < 0:
            new_index = 3
        self.valor = self.COMPASS[new_index]


if __name__ == '__main__':
    # Testando Direcao
    direcao = Direcao()
    print('Direção esperada "Norte":', direcao.valor)

    direcao.girar_a_direita()
    print('Direção esperada "Leste":', direcao.valor)

    direcao.girar_a_direita()
    print('Direção esperada "Sul":', direcao.valor)

    direcao.girar_a_direita()
    print('Direção esperada "Oeste":', direcao.valor)

    direcao.girar_a_direita()
    print('Direção esperada "Norte":', direcao.valor)

    direcao.girar_a_esquerda()
    print('Direção esperada "Oeste":', direcao.valor)

    direcao.girar_a_esquerda()
    print('Direção esperada "Sul":', direcao.valor)

    direcao.girar_a_esquerda()
    print('Direção esperada "Leste":', direcao.valor)

    direcao.girar_a_esquerda()
    print('Direção esperada "Norte":', direcao.valor)
