import os

clientes = []

class Cliente:
    nome = ""
    idade = 0
    div = False
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def info(self):
        print("Nome.: " + self.nome)
        print("Idade: " + int(self.idade))

def Menu():
    os.system('cls') or None
    print("1 - Cadastrar Cliente")
    print("2 - Consultar Cliente")
    print("3 - Excluir Cliente")
    print("4 - Sair")

    opc = input("Entre com a opção desejada: ")

    return opc

def Cadastrar():
    os.system('cls') or None
    