"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:
1) Motor
2) Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
2) Método girar_a_esquerda
  N
O   L
  S
    Exemplo:
    >>> # Testando motor
    >>> from motor import Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> from direcao import Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor


if __name__ == '__main__':
    from motor import Motor
    from direcao import Direcao

    # Testando motor
    motor = Motor()
    print('Velocidade esperada 0:', motor.velocidade)
    motor.acelerar()
    print('Velocidade esperada 1:', motor.velocidade)
    motor.acelerar()
    print('Velocidade esperada 2:', motor.velocidade)
    motor.acelerar()
    print('Velocidade esperada 3:', motor.velocidade)
    motor.frear()
    print('Velocidade esperada 1:', motor.velocidade)
    motor.frear()
    print('Velocidade esperada 0:', motor.velocidade)

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

    # Testando Carro
    carro = Carro(direcao, motor)
    print('Velocidade esperada 0:', carro.calcular_velocidade())
    carro.acelerar()
    print('Velocidade esperada 1:', carro.calcular_velocidade())
    carro.acelerar()
    print('Velocidade esperada 2:', carro.calcular_velocidade())
    carro.frear()
    print('Velocidade esperada 0:', carro.calcular_velocidade())

    print('Direcao esperada "Norte":', carro.calcular_direcao())
    carro.girar_a_direita()
    print('Direcao esperada "Leste":', carro.calcular_direcao())
    carro.girar_a_esquerda()
    print('Direcao esperada "Norte":', carro.calcular_direcao())
    carro.girar_a_esquerda()
    print('Direcao esperada "Oeste":', carro.calcular_direcao())
