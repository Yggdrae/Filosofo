import os
import colorama
import datetime

def main():
    print(colorama.Fore.LIGHTBLUE_EX + "1- Cadastrar Cliente")
    print("2- Consultar Cliente")
    print("3- Excluir Cliente")
    print("4- Sair" + colorama.Fore.RESET)
    op = int(input("Entre com a operação desejada: "))
    return op

class Cliente:
    nome = ""
    nasc= 31/12/99
    CPF = format()
    def __init__(self, nome, nasc, CPF):
        self.nome = nome
        self.nasc = nasc
        self.CPF = CPF
        self.ativo = True

clientes = {}

op = main()

while op != 4:
    if op == 1:
        
#get nome -> array -> 