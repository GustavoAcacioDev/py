import random

computer_alternative = 0
player_alternative = 0
isFirstDrawn = False

def isRock(value):
    if value == 0: return True

def isPaper(value):
    if value == 1: return True

def isScizors(value):
    if value == 2: return True

while computer_alternative == player_alternative:
    if not isFirstDrawn:
        print("Ocorreu um Empate!")

    computer_alternative = random.randint(0, 2)
    player_alternative = int(input('O que você irá escolher? \nDigite 0 para "Pedra", 1 para "Papel" e 2 para "Tesoura":\n'))

    if not player_alternative == 0 or player_alternative == 1 or player_alternative == 2:
        print("Escolha uma opção válida!")

    if isRock(computer_alternative) and isPaper(player_alternative):
        print("A máquina escolheu Pedra e você ganhou!")

    if isPaper(computer_alternative) and isScizors(player_alternative):
        print("A máquina escolheu Papel e você ganhou!")

    if isScizors(computer_alternative) and isRock(player_alternative):
        print("A máquina escolheu Tesoura e você ganhou!")

    if isRock(player_alternative) and isPaper(computer_alternative):
        print("A máquina escolheu Papel e ganhou de você!")

    if isPaper(player_alternative) and isScizors(computer_alternative):
        print("A máquina escolheu Tesoura e ganhou de você!")

    if isScizors(player_alternative) and isRock(computer_alternative):
        print("A máquina escolheu Pedra e ganhou de você!")

