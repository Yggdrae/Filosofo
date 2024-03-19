import os
import random
from colorama import Fore, Back, Style

jogarnovamente = "s"
jogadas = 0
quemJoga=2 #1=CPU 2=Jogador
maxJogadas=9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def attjogo():
    global velha
    global jogadas
    os.system('cls')
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("\nJogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas

    if quemJoga==2 and jogadas<maxJogadas:
        try:
            l=int(input("Linha.: "))
            c=int(input("Coluna: "))
            while velha[l][c] != " ":
                os.system('cls')
                l=int(input("Linha.: "))
                c=int(input("Coluna: "))
            velha[l][c]="X"
            quemJoga = 1
            jogadas+=1
        except:
            print("Linha e/ou Coluna invalidas!")
            os.system('pause')
            os.system('cls')

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l=random.randrange(0, 3)
        c=random.randrange(0, 3)
        while velha[l][c] != " ":
            l=random.randrange(0, 2)
            c=random.randrange(0, 2)
        velha[l][c]="O"
        quemJoga = 2
        jogadas+=1

def verifvit():
    global velha
    vit = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vit = "n"
        #Verifica Linhas
        il = ic = 0
        while il < 3:
            soma=0
            ic=0
            while ic < 3:
                if velha[il][ic] == s:
                    soma+=1
                ic+=1
            il+=1
        if soma == 3:
            vit = s
            break
        if vit!="n":
            break
        #Verifica Colunas
        il = ic = 0
        while ic < 3:
            soma=0
            il=0
            while il < 3:
                if velha[il][ic] == s:
                    soma+=1
                il+=1
            ic+=1
        if soma == 3:
            vit = s
            break
        if vit!="n":
            break
        #Verifica Diagonal 1
        soma = 0
        idiag = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
               soma+=1
            idiag+=1
        if soma == 3:
            vit = s
            break
        #Verifica Diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >=0:
            if velha[idiagl][idiagc] == s:
               soma+=1
            idiagl+=1
            idiagc-=1
        if soma == 3:
            vit = s
            break
    return vit

def redef():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga=2 #1=CPU 2=Jogador
    maxJogadas=9
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarnovamente=="s":
    while True:
        attjogo()
        jogadorJoga()
        cpuJoga()
        attjogo()
        vit = verifvit()
        if vit != "n" or jogadas>=maxJogadas:
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if vit == "X" or vit == "O":
        print("Jogador " + vit + " venceu")
    jogarnovamente = input(Fore.BLUE + "Jogar Novamente? s/n: ")
    redef()