class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


if __name__ == '__main__':
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

