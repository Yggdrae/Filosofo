import random
import os

erros = 0
sorteado = random.randrange(0,100)

os.system('cls')

jogador = int(input("Digite o numero: "))

while jogador != sorteado:
    os.system('cls')
    if sorteado > jogador:
        print("O numero sorteado é MAIOR")
    elif sorteado < jogador:
        print("O numero sorteado é MENOR")
    erros+=1

    jogador = int(input("Digite o numero: "))    

print("Voce acertou em " + str(erros+1) + " tentativas")