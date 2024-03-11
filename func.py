import os

def cadastro(nome):
    file = open("cadastros.txt", "a+")
    file.write(nome + "\n")
    file.close()

def consulta():
    consul = input("Entre com o nome a ser consultado: ")
    file = open("cadastros.txt", "r+")
    print(file.read())
    os.system('pause')
    file.close()

op = 0

while op != 4:
    os.system('cls')
    print("1- Cadastrar novo\n2- Editar\n3- Consultar\n4- Sair")
    op = input("Entre com a operação desejada: ")

    if op == "1":
        cadastro(input("Entre com seu nome: "))
    elif op == "3":
        consulta()
        op = 0
    elif op == "4":
        print("Encerrando o programa")
        break